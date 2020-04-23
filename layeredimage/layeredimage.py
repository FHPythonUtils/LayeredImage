""" LayeredImage class """

from PIL import Image
from layeredimage.layergroup import LayerGroupTypes, Layer
from layeredimage.blend import blendLayers

class LayeredImage:
	""" A representation of a layered image such as an ora """
	def __init__(self, layersAndGroups, dimensions=None, **kwargs):
		# Write here
		self.layersAndGroups = layersAndGroups
		# Read only
		self.groups = self.extractGroups()
		self.layers = self.extractLayers()
		# If the user does not specify the dimentions use the largest x and y of
		# the layers and groups
		self.dimensions = dimensions
		if dimensions is None:
			layerDimens = [layerOrGroup.dimensions for layerOrGroup in layersAndGroups]
			self.dimensions = (max([dimensions[0] for dimentions in layerDimens]),
			max([dimensions[1] for dimentions in layerDimens]))
		self.extras = kwargs

	# Get, set and remove layers or groups
	def getLayerOrGroup(self, index):
		""" Get a LayerOrGroup """
		return self.layersAndGroups[index]

	def addLayerOrGroup(self, LayerOrGroup):
		""" Add a LayerOrGroup """
		self.layersAndGroups.append(LayerOrGroup)

	def insertLayerOrGroup(self, LayerOrGroup, index):
		""" Insert a LayerOrGroup at a specific index """
		self.layersAndGroups.insert(index, LayerOrGroup)

	def removeLayerOrGroup(self, index):
		""" Remove a LayerOrGroup at a specific index """
		self.layersAndGroups.pop(index)

	# The user may wish to add an image directly
	def addLayerRaster(self, image, name):
		""" Raster an image and add as a layer """
		layer = rasterImageOA(image, self.dimensions)
		self.addLayerOrGroup(Layer(layer, name, self.dimensions))

	def insertLayerRaster(self, image, name, index):
		""" Raster an image and insert the layer """
		layer = rasterImageOA(image, self.dimensions)
		self.insertLayerOrGroup(Layer(layer, name, self.dimensions), index)


	# The user may want to flatten the layers
	def getFlattenLayers(self, ignoreHidden=True):
		""" Return an image for all flattened layers """
		return flattenAll(self.layersAndGroups, self.dimensions, ignoreHidden)

	def getFlattenTwoLayers(self, background, foreground, ignoreHidden=True):
		""" Return an image for two flattened layers """
		flattenedSoFar = flattenLayerOrGroup(self.layersAndGroups[background],
		self.dimensions, ignoreHidden=ignoreHidden)
		return flattenLayerOrGroup(self.layersAndGroups[foreground], self.dimensions,
		flattenedSoFar,	ignoreHidden=ignoreHidden)

	def flattenTwoLayers(self, background, foreground, ignoreHidden=True):
		""" Flatten two layers """
		image = self.getFlattenTwoLayers(background, foreground, ignoreHidden)
		self.removeLayerOrGroup(foreground)
		self.layersAndGroups[background] = Layer(image,
		self.layersAndGroups[background].name + " (flattened)", self.dimensions)

	def flattenLayers(self, ignoreHidden=True):
		""" Flatten all layers """
		image = self.getFlattenLayers(ignoreHidden)
		self.layersAndGroups[0] = Layer(image,
		self.layersAndGroups[0].name + " (flattened)", self.dimensions)
		for layer in range(1, len(self.layersAndGroups)):
			self.removeLayerOrGroup(layer)

	# The user may hate groups and just want the layers... or just want the
	# groups
	def extractLayers(self):
		""" Extract the layers from the image """
		layers = []
		for layerOrGroup in	self.layersAndGroups:
			if layerOrGroup.type == LayerGroupTypes.LAYER:
				layers.append(layerOrGroup)
			elif layerOrGroup.type == LayerGroupTypes.GROUP:
				for layer in layerOrGroup.layers:
					# 'Raster' the layer
					layers.append(Layer(layer.name, layer.image,
					(max(layer.dimensions[0], layerOrGroup.dimensions[0]),
					max(layer.dimensions[1], layerOrGroup.dimensions[1])),
					(layerOrGroup.offsets[0] + layer.offsets[0],
					layerOrGroup.offsets[1] + layer.offsets[1]),
					layerOrGroup.opacity * layer.opacity,
					layerOrGroup.visible and layer.visible))
		return layers

	def updateLayers(self):
		""" Update the layers from the image """
		self.layers = self.extractLayers()

	def extractGroups(self):
		""" Extract the groups from the image """
		return [_layerOrGroup for _layerOrGroup in
			self.layersAndGroups if _layerOrGroup.type == LayerGroupTypes.GROUP]

	def updateGroups(self):
		""" Update the groups from the image """
		self.groups = self.extractGroups()

def rasterImageOA(image, size, alpha=1.0, offsets=(0, 0)):
	""" Rasterise an image with offset and alpha to a given size"""
	imageOffset = rasterImageOffset(image, size, offsets)
	return Image.blend(Image.new("RGBA", size), imageOffset, alpha)

def rasterImageOffset(image, size, offsets=(0, 0)):
	""" Rasterise an image with offset to a given size"""
	imageOffset = Image.new("RGBA", size)
	imageOffset.paste(image.convert("RGBA"), offsets, image.convert("RGBA"))
	return imageOffset

def flattenLayerOrGroup(layerOrGroup, imageDimensions, flattenedSoFar=None, ignoreHidden=True):
	"""Flatten a layer or group on to an image of what has already been
	flattened

	Args:
		layerOrGroup (Layer|Group): A layer or a group of layers
		imageDimensions ((int, int)): size of the image
		flattenedSoFar (PIL.Image, optional): the image of what has already
		been flattened. Defaults to None.
		ignoreHidden (bool, optional): ignore layers that are hidden. Defaults
		to True.

	Returns:
		PIL.Image: Flattened image
	"""
	if not ignoreHidden and not layerOrGroup.visible:
		foregroundRaster = Image.new("RGBA", imageDimensions)
	elif layerOrGroup.type == LayerGroupTypes.GROUP:
		foregroundRaster = flattenAll(layerOrGroup.layers, imageDimensions, ignoreHidden)
	else:
		# Get a raster image and apply blending
		foregroundRaster = rasterImageOffset(layerOrGroup.image, imageDimensions,
		layerOrGroup.offsets)
		if flattenedSoFar is None:
			return foregroundRaster
	return blendLayers(flattenedSoFar, foregroundRaster, layerOrGroup.blendmode)


def flattenAll(layers, imageDimensions, ignoreHidden):
	"""Flatten a list of layers and groups

	Args:
		layers ([Layer|Group]): A list of layers and groups
		imageDimensions ((int, int)): size of the image
		been flattened. Defaults to None.
		ignoreHidden (bool, optional): ignore layers that are hidden. Defaults
		to True.

	Returns:
		PIL.Image: Flattened image
	"""
	flattenedSoFar = flattenLayerOrGroup(layers[0], imageDimensions, ignoreHidden=ignoreHidden)
	for layer in range(1, len(layers)):
		flattenedSoFar = flattenLayerOrGroup(layers[layer], imageDimensions,
		flattenedSoFar=flattenedSoFar, ignoreHidden=ignoreHidden)
	return flattenedSoFar
