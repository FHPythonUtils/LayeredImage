""" Base class """
from __future__ import annotations
from typing import Any, Optional
from PIL import Image
from layeredimage.blend import BlendType

#pylint: disable=too-few-public-methods
#pylint: disable=too-many-arguments

class LayerGroup:
	""" A representation of an image layer or group """
	def __init__(self, name: str, dimensions: tuple[int, int],
	offsets: tuple[int, int]=(0, 0), opacity: float =1.0, visible: bool=True,
	blendmode: BlendType=BlendType.NORMAL, **kwargs: Any):
		""" A representation of an image layer or group

		Args:
			name (str): Name of the layer or group
			dimensions ((int, int)): A tuple representing the dimensions in
			pixels
			offsets (tuple, optional): A tuple representing the left and top
			offsets in pixels. Defaults to (0, 0).
			opacity (float, optional): A float representing the alpha value
			where 0 is invisible and 1 is fully visible. Defaults to 1.0.
			visible (bool, optional): Is the layer visible to the user (this
			is often configured per layer or per group by an 'eye' icon).
			Defaults to True.
		"""
		self.name = name
		self.offsets = offsets
		self.opacity = opacity
		self.visible = visible
		self.dimensions = dimensions
		self.blendmode = blendmode
		self.extras = kwargs

	def __repr__(self):
		return "<LayeredImage " + " \"" + self.name + "\" (" + str(self.dimensions[0]) + "x" + str(
			self.dimensions[1]) + ")>"

	def json(self) -> dict[str, Any]:
		""" Get the object as a dict """
		return {"name": self.name, "offsets": self.offsets, "opacity": self.opacity,
		"visible": self.visible, "dimensions": self.dimensions, "blendmode": self.blendmode.name}


class Layer(LayerGroup):
	""" A representation of an image layer """
	def __init__(self, name: str, image: Image.Image, dimensions: tuple[int, int],
	offsets: tuple[int, int]=(0, 0), opacity: float =1.0, visible: bool=True,
	blendmode: BlendType=BlendType.NORMAL):
		""" A representation of an image layer

		Args:
			name (str): Name of the layer or group
			image (Image.Image): A PIL Image
			dimensions (tuple[int, int]): A tuple representing the dimensions in
			pixels
			offsets (tuple[int, int], optional): A tuple representing the left and top
			offsets in pixels. Defaults to (0, 0).
			opacity (float, optional): A float representing the alpha value
			where 0 is invisible and 1 is fully visible. Defaults to 1.0.
			visible (bool, optional): Is the layer visible to the user (this
			is often configured per layer or per group by an 'eye' icon).
			Defaults to True.
		"""
		super().__init__(name, dimensions, offsets=offsets, opacity=opacity,
		visible=visible, blendmode=blendmode)
		self.image = image

		# If the user does not specify the dimensions use image.size
		self.dimensions = dimensions
		if dimensions is None:
			self.dimensions = image.size

	def json(self) -> dict[str, Any]:
		""" Get the object as a dict """
		return {"name": self.name, "offsets": self.offsets, "opacity": self.opacity,
		"visible": self.visible, "dimensions": self.dimensions, "type": "LAYER",
		"blendmode": self.blendmode.name}


class Group(LayerGroup):
	""" A representation of an image group """
	def __init__(self, name: str, layers:list[Layer],
	dimensions: Optional[tuple[int, int]]=None,
	offsets: tuple[int, int]=(0, 0), opacity: float =1.0, visible: bool=True,
	blendmode: BlendType=BlendType.NORMAL):
		""" A representation of an image group

		Args:
			name (str): Name of the layer or group
			layers (layeredimage.Layer[]): A list of layers where the next
			index stacks upon the previous layer
			dimensions ((int, int)): A tuple representing the dimensions in
			pixels
			offsets (tuple, optional): A tuple representing the left and top
			offsets in pixels. Defaults to (0, 0).
			opacity (float, optional): A float representing the alpha value
			where 0 is invisible and 1 is fully visible. Defaults to 1.0.
			visible (bool, optional): Is the layer visible to the user (this
			is often configured per layer or per group by an 'eye' icon).
			Defaults to True.
		"""
		# Initialise dimens to 0 and then calculate as below
		super().__init__(name, (0, 0), offsets=offsets, opacity=opacity,
		visible=visible, blendmode=blendmode)
		self.layers = layers

		# If the user does not specify the dimensions use the largest x and y of
		# the layers
		if dimensions is not None:
			self.dimensions = dimensions
		else:
			layerDimens = [layer.dimensions for layer in layers]
			self.dimensions = (max([dimensions[0] for dimensions in layerDimens]),
			max([dimensions[1] for dimensions in layerDimens]))

	def json(self) -> dict[str, Any]:
		""" Get the object as a dict """
		layers = [layer.json() for layer in self.layers]
		return {"name": self.name, "offsets": self.offsets, "opacity": self.opacity,
		"visible": self.visible, "dimensions": self.dimensions, "type": "GROUP",
		"blendmode": self.blendmode.name, "layers": layers}
