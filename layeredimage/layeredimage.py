"""LayeredImage class."""

from __future__ import annotations

from typing import Any

import numpy as np
from blendmodes.blend import blendLayersArray
from PIL import Image

from layeredimage.layergroup import Group, Layer


class LayeredImage:
	"""A representation of a layered image such as an ora."""

	def __init__(
		self,
		layersAndGroups: list[Layer | Group],
		dimensions: tuple[int, int] | None = None,
		**kwargs: dict[str, Any],
	) -> None:
		"""LayeredImage - representation of a layered image.

		Args:
		----
			layersAndGroups (list[Layer, Group]): List of layers and groups
			dimensions (tuple[int, int], optional): dimensions of the canvas. Defaults to None.
			**kwargs (Any): add any keyword args to self.extras

		"""
		# Write here
		self.layersAndGroups = layersAndGroups
		# Read only
		self.groups = self.extractGroups()
		self.layers = self.extractLayers()
		# If the user does not specify the dimensions use the largest x and y of
		# the layers and groups
		self.dimensions = dimensions or (0, 0)
		if dimensions is None:
			layerDimens = [layerOrGroup.dimensions for layerOrGroup in layersAndGroups]
			self.dimensions = (
				max(layerDimen[0] for layerDimen in layerDimens),
				max(layerDimen[1] for layerDimen in layerDimens),
			)
		self.extras = kwargs

	def __repr__(self) -> str:
		"""Get the string representation."""
		return self.__str__()

	def __str__(self) -> str:
		"""Get the string representation."""
		return (
			f"<LayeredImage ({self.dimensions[0]}x{self.dimensions[1]}) with "
			f"{len(self.layersAndGroups)} children>"
		)

	def json(self) -> dict[str, Any]:
		"""Get the object as a dict."""
		layersAndGroups = [layerOrGroup.json() for layerOrGroup in self.layersAndGroups]
		return {"dimensions": self.dimensions, "layersAndGroups": layersAndGroups}

	# Get, set and remove layers or groups
	def getLayerOrGroup(self, index: int) -> Layer | Group:
		"""Get a LayerOrGroup."""
		return self.layersAndGroups[index]

	def addLayerOrGroup(self, layerOrGroup: Layer | Group) -> None:
		"""Add a LayerOrGroup."""
		self.layersAndGroups.append(layerOrGroup)

	def insertLayerOrGroup(self, layerOrGroup: Layer | Group, index: int) -> None:
		"""Insert a LayerOrGroup at a specific index."""
		self.layersAndGroups.insert(index, layerOrGroup)

	def removeLayerOrGroup(self, index: int) -> None:
		"""Remove a LayerOrGroup at a specific index."""
		self.layersAndGroups.pop(index)

	# The user may want to flatten the layers
	def getFlattenLayers(self) -> Image.Image:
		"""Return an image for all flattened layers."""

		project_image = np.zeros((self.dimensions[1], self.dimensions[0], 4), dtype=np.uint8)
		for layerOrGroup in self.layersAndGroups:
			if layerOrGroup.visible:
				project_image = render(layerOrGroup, project_image)

		return Image.fromarray(np.uint8(np.around(project_image, 0)))

	# The user may hate groups and just want the layers... or just want the
	# groups
	def extractLayers(self) -> list[Layer]:
		"""Extract the layers from the image."""
		layers = []
		for layerOrGroup in self.layersAndGroups:
			if isinstance(layerOrGroup, Layer):
				layers.append(layerOrGroup)
			else:
				for layer in layerOrGroup.layers:
					# Render the layer
					layers.append(
						Layer(
							name=layer.name,
							image=layer.image,
							dimensions=(
								max(layer.dimensions[0], layerOrGroup.dimensions[0]),
								max(layer.dimensions[1], layerOrGroup.dimensions[1]),
							),
							offsets=(
								layerOrGroup.offsets[0] + layer.offsets[0],
								layerOrGroup.offsets[1] + layer.offsets[1],
							),
							opacity=layerOrGroup.opacity * layer.opacity,
							visible=layerOrGroup.visible and layer.visible,
						)
					)
		return layers

	def updateLayers(self) -> None:
		"""Update the layers from the image."""
		self.layers = self.extractLayers()

	def extractGroups(self) -> list[Group]:
		"""Extract the groups from the image."""
		return [
			_layerOrGroup
			for _layerOrGroup in self.layersAndGroups
			if isinstance(_layerOrGroup, Group)
		]

	def updateGroups(self) -> None:
		"""Update the groups from the image."""
		self.groups = self.extractGroups()


def render(layerOrGroup: Layer | Group, project_image: np.ndarray) -> np.ndarray:
	"""Flatten a layer or group on to an image of what has already been flattened.

	Args:
	----
		layerOrGroup (Layer, Group): A layer or a group of layers
		project_image (np.ndarray, optional): the image of what has already
		been flattened.

	Returns:
	-------
		np.ndarray: Flattened image

	"""
	if isinstance(layerOrGroup, Layer):
		return blendLayersArray(
			project_image,
			layerOrGroup.image,
			layerOrGroup.blendmode,
			layerOrGroup.opacity,
			layerOrGroup.offsets,
		)
	if isinstance(layerOrGroup, Group):
		group_image = np.zeros(
			(layerOrGroup.dimensions[1], layerOrGroup.dimensions[0], 4), dtype=np.uint8
		)
		for item in layerOrGroup.layers:
			group_image = render(item, group_image)
		return blendLayersArray(
			project_image,
			group_image,
			layerOrGroup.blendmode,
			layerOrGroup.opacity,
			layerOrGroup.offsets,
		)

	msg = "Unsupported type encountered"
	raise TypeError(msg)
