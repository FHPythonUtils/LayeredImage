""" Base class """

from enum import Enum
class LayerGroupTypes(Enum):
	""" Can be a LAYER, GROUP, or UNDEFINED """
	UNDEFINED = 0
	LAYER = 1
	GROUP = 2

class LayerGroup:
	""" A representation of an image layer or group """
	def __init__(self, name, dimensions, offsets=(0, 0), opacity=1.0, visible=True,
	layerGroup=LayerGroupTypes.LAYER, **kwargs):
		""" A representation of an image layer or group

		Args:
			name (string): Name of the layer or group
			dimensions ((int, int)): A tuple representing the dimentions in
			pixels
			offsets (tuple, optional): A tuple representing the left and top
			offsets in pixels. Defaults to (0, 0).
			opacity (float, optional): A float representing the alpha value
			where 0 is invisible and 1 is fully visible. Defaults to 1.0.
			visible (bool, optional): Is the layer visible to the user (this
			is often configured per layer or per group by an 'eye' icon).
			Defaults to True.
			layerGroup ([type], optional): Type LAYER, GROUP, or UNDEFINED.
			Defaults to LayerGroupTypes.LAYER.
		"""
		self.name = name
		self.offsets = offsets
		self.opacity = opacity
		self.visible = visible
		self.dimensions = dimensions
		self.type = layerGroup
		self.extras = kwargs

	def __repr__(self):
		return "<LayeredImage " + ("Group" if self.type == LayerGroupTypes.GROUP else "Layer") + " \"" + self.name + "\" (" + str(self.dimensions[0]) + "x" + str(self.dimensions[1]) + ")>"


class Layer(LayerGroup):
	""" A representation of an image layer """
	def __init__(self, name, image, dimensions=None, offsets=(0, 0), opacity=1.0, visible=True):
		""" A representation of an image layer

		Args:
			name (string): Name of the layer or group
			image (PIL.Image): A PIL Image
			dimensions ((int, int)): A tuple representing the dimentions in
			pixels
			offsets (tuple, optional): A tuple representing the left and top
			offsets in pixels. Defaults to (0, 0).
			opacity (float, optional): A float representing the alpha value
			where 0 is invisible and 1 is fully visible. Defaults to 1.0.
			visible (bool, optional): Is the layer visible to the user (this
			is often configured per layer or per group by an 'eye' icon).
			Defaults to True.
		"""
		super().__init__(name, dimensions, offsets=offsets, opacity=opacity, visible=visible)
		self.image = image

		# If the user does not specify the dimentions use image.size
		self.dimensions = dimensions
		if dimensions is None:
			self.dimensions = image.size



class Group(LayerGroup):
	""" A representation of an image group """
	def __init__(self, name, layers, dimensions=None, offsets=(0, 0), opacity=1.0, visible=True):
		""" A representation of an image group

		Args:
			name (string): Name of the layer or group
			layers (layeredimage.Layer[]): A list of layers where the next
			index stacks upon the previous layer
			dimensions ((int, int)): A tuple representing the dimentions in
			pixels
			offsets (tuple, optional): A tuple representing the left and top
			offsets in pixels. Defaults to (0, 0).
			opacity (float, optional): A float representing the alpha value
			where 0 is invisible and 1 is fully visible. Defaults to 1.0.
			visible (bool, optional): Is the layer visible to the user (this
			is often configured per layer or per group by an 'eye' icon).
			Defaults to True.
		"""
		super().__init__(name, dimensions, offsets=offsets, opacity=opacity,
		visible=visible, layerGroup=LayerGroupTypes.GROUP)
		self.layers = layers

		# If the user does not specify the dimentions use the largest x and y of
		# the layers
		self.dimensions = dimensions
		if dimensions is None:
			layerDimens = [layer.dimensions for layer in layers]
			self.dimensions = (max([dimensions[0] for dimentions in layerDimens]),
			max([dimensions[1] for dimentions in layerDimens]))
