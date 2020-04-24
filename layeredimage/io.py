""" Do file io """

# To avoid throwing import errors for the sake of it, specialised imports are
# to be scoped to the function
# pylint: disable=import-outside-toplevel

from os.path import exists
from sys import version_info
from metprint import LogType, Logger, FHFormatter
from layeredimage.layergroup import LayerGroupTypes, Layer, Group
from layeredimage.layeredimage import LayeredImage, rasterImageOA
from layeredimage.blend import BlendType

def extNotRecognised(fileName):
	""" Output the file extension not recognised error """
	exts = ["ora", "psd", "xcf", "pdn", "tif", "tiff"]
	Logger(FHFormatter()).logPrint("File extension is not recognised for file: " +
	fileName + "! Must be " + "one of \"" + ", \"".join(exts) + "\"", LogType.ERROR)

def openLayerImage(file):
	"""Open a layer image file into a layer image object

	Args:
		file (string): path/ filename

	Returns:
		LayeredImage: a layered image object
	"""
	if not exists(file):
		Logger(FHFormatter()).logPrint(file + " does not exist", LogType.ERROR)
		raise FileExistsError
	if file[-3:] == "ora":
		return openLayer_ORA(file)
	if file[-3:] == "psd":
		return openLayer_PSD(file)
	if file[-3:] == "xcf":
		return openLayer_XCF(file)
	if file[-3:] == "pdn":
		return openLayer_PDN(file)
	if file[-3:] == "tif" or file[-4:] == "tiff":
		return openLayer_TIFF(file)
	Logger(FHFormatter()).logPrint("File extension is not recognised!", LogType.ERROR)
	extNotRecognised(file)
	raise ValueError

def saveLayerImage(fileName, layeredImage):
	"""Save a layered image to a file

	Args:
		fileName (string): path/ filename
		layeredImage (LayeredImage): the layered image to save
	"""
	if fileName[-3:] == "ora":
		return saveLayer_ORA(fileName, layeredImage)
	if fileName[-3:] == "psd":
		return saveLayer_PSD(fileName, layeredImage)
	if fileName[-3:] == "xcf":
		return saveLayer_XCF(fileName, layeredImage)
	if fileName[-3:] == "pdn":
		return saveLayer_PDN(fileName, layeredImage)
	if fileName[-3:] == "tif" or fileName[-4:] == "tiff":
		return saveLayer_TIFF(fileName, layeredImage)
	extNotRecognised(fileName)
	raise ValueError

def exportFlatImage(fileName, layeredImage):
	""" Export the layered image to a unilayer image file """
	layeredImage.getFlattenLayers().save(fileName)

def blendModeLookup(blendmode, blendLookup, default=BlendType.NORMAL):
	""" Get the blendmode from a lookup table """
	if blendmode not in blendLookup:
		Logger(FHFormatter()).logPrint(str(blendmode) + " is not currently supported!", LogType.WARNING)
		return default
	return blendLookup[blendmode]

#### ORA ####
def openLayer_ORA(file):
	""" Open an .ora file into a layered image """
	from pyora import Project, TYPE_LAYER
	# Not implemented color luminosity hue saturation
	blendLookup = {"svg:src-over": BlendType.NORMAL, "svg:multiply": BlendType.MULTIPLY,
	"svg:color-burn": BlendType.COLOURBURN,	"svg:color-dodge": BlendType.COLOURDODGE,
	"svg:": BlendType.REFLECT, "svg:overlay": BlendType.OVERLAY,
	"svg:difference": BlendType.DIFFERENCE,	"svg:lighten": BlendType.LIGHTEN,
	"svg:darken": BlendType.DARKEN, "svg:screen": BlendType.SCREEN,
	"svg:hard-light": BlendType.HARDLIGHT, "svg:soft-light": BlendType.SOFTLIGHT}
	layersAndGroups = []
	project = Project.load(file)
	for layerOrGroup in project.children[::-1]:
		if layerOrGroup.type == TYPE_LAYER:
			layersAndGroups.append(Layer(layerOrGroup.name, layerOrGroup.get_image_data(True),
			layerOrGroup.dimensions, layerOrGroup.offsets, layerOrGroup.opacity, layerOrGroup.visible,
			blendModeLookup(layerOrGroup.composite_op, blendLookup)))
		else:
			layers = []
			for layer in list(layerOrGroup.children)[::-1]:
				layers.append(Layer(layer.name, layer.get_image_data(True),
				layer.dimensions, layer.offsets,
				layer.opacity, layer.visible,
				blendModeLookup(layerOrGroup.composite_op, blendLookup)))
			layersAndGroups.append(Group(layerOrGroup.name, layers, project.dimensions, layerOrGroup.offsets,
			layerOrGroup.opacity, layerOrGroup.visible,
			blendModeLookup(layerOrGroup.composite_op, blendLookup)))
	return LayeredImage(layersAndGroups, project.dimensions)

def saveLayer_ORA(fileName, layeredImage):
	""" Save a layered image as .ora """
	from pyora import Project
	blendLookup = {BlendType.NORMAL: "svg:src-over", BlendType.MULTIPLY: "svg:multiply",
	BlendType.COLOURBURN: "svg:color-burn",	BlendType.COLOURDODGE: "svg:color-dodge",
	BlendType.REFLECT: "svg:",	BlendType.OVERLAY: "svg:overlay",
	BlendType.DIFFERENCE: "svg:difference",	BlendType.LIGHTEN: "svg:lighten",
	BlendType.DARKEN: "svg:darken", BlendType.SCREEN: "svg:screen",
	BlendType.SOFTLIGHT: "svg:soft-light", BlendType.HARDLIGHT: "svg:hard-light"}
	project = Project.new(layeredImage.dimensions[0], layeredImage.dimensions[1])
	for layerOrGroup in layeredImage.layersAndGroups:
		if layerOrGroup.type == LayerGroupTypes.LAYER:
			project = addLayer_ORA(project, layerOrGroup, blendLookup)
		else:
			group = project.add_group(layerOrGroup.name,
			offsets=layerOrGroup.offsets, opacity=layerOrGroup.opacity,
			visible=layerOrGroup.visible,
			composite_op=blendModeLookup(layerOrGroup.blendmode, blendLookup, "svg:src-over"))
			for layer in layerOrGroup.layers:
				group = addLayer_ORA(group, layer, blendLookup)
	Project.save = save_ORA_fix
	project.save(fileName)

def addLayer_ORA(project, layer, blendLookup):
	""" Update the project with a shiny new layer """
	project.add_layer(layer.image, layer.name, offsets=layer.offsets,
	opacity=layer.opacity, visible=layer.visible,
	composite_op=blendModeLookup(layer.blendmode, blendLookup, "svg:src-over"))
	return project

def save_ORA_fix(self, path_or_file, composite_image=None, use_original=False):
	""" Patch the Project.save function from pyora 3.0 with a newer version -Future
	This snippet is MIT License Copyright (c) 2019 Paul Jewell
	"""
	# This is a patch, so I'm going to need to access what I please
	# pylint: disable=protected-access
	import zipfile
	from defusedxml import ElementTree as ET
	from pyora.Render import Renderer, make_thumbnail
	from pyora import TYPE_LAYER
	with zipfile.ZipFile(path_or_file, 'w') as zipref:
		zipref.writestr('mimetype', "image/openraster".encode())
		zipref.writestr('stack.xml', ET.tostring(self._elem_root, method='xml'))
		if not composite_image:
			if use_original and self._extracted_merged_image:
				composite_image = self._extracted_merged_image
			else:
				r = Renderer(self)
				composite_image = r.render()
		self._zip_store_image(zipref, 'mergedimage.png', composite_image)
		make_thumbnail(composite_image)  # works in place
		self._zip_store_image(zipref, 'Thumbnails/thumbnail.png', composite_image)

		for layer in self.children_recursive:
			if layer.type == TYPE_LAYER:
				self._zip_store_image(zipref, layer['src'], layer.get_image_data(True))
	# pylint: enable=protected-access


#### PSD ####
def openLayer_PSD(file):
	""" Open a .psd file into a layered image """
	from psd_tools import PSDImage
	blendLookup = {"normal": BlendType.NORMAL, "multiply": BlendType.MULTIPLY,
	"color burn": BlendType.COLOURBURN, "color dodge": BlendType.COLOURDODGE,
	"overlay": BlendType.OVERLAY, "difference": BlendType.DIFFERENCE,
	"subtract": BlendType.NEGATION, "lighten": BlendType.LIGHTEN,
	"darken": BlendType.DARKEN, "screen": BlendType.SCREEN,
	"soft light": BlendType.SOFTLIGHT, "hard light": BlendType.HARDLIGHT}
	layersAndGroups = []
	project = PSDImage.load(file)
	for layerOrGroup in project.layers[::-1]:
		if layerOrGroup.is_group():
			layers = []
			for layer in layerOrGroup.layers:
				layers.append(Layer(layer.name, layer.as_PIL(), (layer.width,
				layer.height), (layer.left, layer.top),
				layer.opacity / 255, layer.visible,
				blendModeLookup(layer.blend_mode, blendLookup)))
			layersAndGroups.append(Group(layerOrGroup.name, layers, (layerOrGroup.width,
			layerOrGroup.height), (layerOrGroup.left, layerOrGroup.top),
			layerOrGroup.opacity / 255, layerOrGroup.visible,
			blendModeLookup(layerOrGroup.blend_mode, blendLookup)))
		else:
			layersAndGroups.append(
			Layer(layerOrGroup.name, layerOrGroup.as_PIL(), (layerOrGroup.width,
			layerOrGroup.height), (layerOrGroup.left, layerOrGroup.top),
			layerOrGroup.opacity / 255, layerOrGroup.visible,
			blendModeLookup(layerOrGroup.blend_mode, blendLookup)))
	return LayeredImage(layersAndGroups, (project.width, project.height))


def saveLayer_PSD(_fileName, _layeredImage):
	""" Save a layered image as .psd """
	Logger(FHFormatter()).logPrint("Saving PSDs is not implemented in psd-tools3 - " +
	"this is present in psd-tools, however, installing it on Windows is difficult so " +
	"I am not currently using this library", LogType.ERROR)
	raise NotImplementedError


#### XCF ####
def openLayer_XCF(file):
	""" Open an .xcf file into a layered image """
	from gimpformats_unofficial.gimpXcfDocument import GimpDocument
	blendLookup = {0: BlendType.NORMAL, 3: BlendType.MULTIPLY,
	7: BlendType.ADDITIVE, 17: BlendType.COLOURBURN, 16: BlendType.COLOURDODGE,
	5: BlendType.OVERLAY, 6: BlendType.DIFFERENCE,
	8: BlendType.NEGATION, 10: BlendType.LIGHTEN,
	9: BlendType.DARKEN, 4: BlendType.SCREEN, 52: BlendType.XOR,
	28: BlendType.NORMAL, 30: BlendType.MULTIPLY,
	33: BlendType.ADDITIVE, 43: BlendType.COLOURBURN, 42: BlendType.COLOURDODGE,
	23: BlendType.OVERLAY, 32: BlendType.DIFFERENCE,
	34: BlendType.NEGATION, 36: BlendType.LIGHTEN,
	35: BlendType.DARKEN, 31: BlendType.SCREEN,
	18: BlendType.HARDLIGHT, 19: BlendType.SOFTLIGHT,
	44: BlendType.HARDLIGHT, 45: BlendType.SOFTLIGHT}
	project = GimpDocument(file)
	# Iterate the layers and create a list of layers for each group, then remove
	# these from the project layers
	layers = project.layers[::-1]
	index = 0
	groupIndex = 0
	groupLayers = [[]]
	while index < len(layers):
		layerOrGroup = layers[index]
		if layerOrGroup.isGroup:
			index -= 1
			while layers[index].itemPath is not None:
				layer = layers[index]
				groupLayers[groupIndex].append(Layer(layer.name, layer.image,
				(layer.width, layer.height), (layer.xOffset, layer.yOffset),
				layer.opacity, layer.visible,
				blendModeLookup(layer.blendMode, blendLookup)))
				layers.pop(index)
				index -= 1
			index += 2
			groupIndex += 1
			groupLayers.append([])
		else:
			index += 1
	# Iterate the clean project layers and add the group layers in
	groupIndex = 0
	layersAndGroups = []
	for layerOrGroup in layers:
		if layerOrGroup.isGroup:
			layersAndGroups.append(Group(layerOrGroup.name, groupLayers[groupIndex][::-1],
				(layerOrGroup.width, layerOrGroup.height), (layerOrGroup.xOffset,
				layerOrGroup.yOffset), layerOrGroup.opacity, layerOrGroup.visible,
				blendModeLookup(layerOrGroup.blendMode, blendLookup)))
			groupIndex += 1
		else:
			layersAndGroups.append(Layer(layerOrGroup.name, layerOrGroup.image,
				(layerOrGroup.width, layerOrGroup.height), (layerOrGroup.xOffset,
				layerOrGroup.yOffset), layerOrGroup.opacity, layerOrGroup.visible,
				blendModeLookup(layerOrGroup.blendMode, blendLookup)))

	return LayeredImage(layersAndGroups, (project.width, project.height))


def saveLayer_XCF(fileName, layeredImage):
	""" Save a layered image as .xcf """
	Logger(FHFormatter()).logPrint("Saving XCFs is not implemented in gimpformats - " +
	"this is a little misleading as functions are pressent, however these are not " +
	"functional", LogType.ERROR)
	raise NotImplementedError


#### PDN ####
def openLayer_PDN(file):
	""" Open a .pdn file into a layered image """
	from pypdn.reader import read, BlendType as PDNBlend
	from PIL import Image
	blendLookup = {PDNBlend.Normal: BlendType.NORMAL, PDNBlend.Multiply: BlendType.MULTIPLY,
	PDNBlend.Additive: BlendType.ADDITIVE, PDNBlend.ColorBurn: BlendType.COLOURBURN,
	PDNBlend.ColorDodge: BlendType.COLOURDODGE, PDNBlend.Reflect: BlendType.REFLECT,
	PDNBlend.Glow: BlendType.GLOW, PDNBlend.Overlay: BlendType.OVERLAY,
	PDNBlend.Difference: BlendType.DIFFERENCE, PDNBlend.Negation: BlendType.NEGATION,
	PDNBlend.Lighten: BlendType.LIGHTEN, PDNBlend.Darken: BlendType.DARKEN,
	PDNBlend.Screen: BlendType.SCREEN, PDNBlend.XOR: BlendType.XOR}
	project = read(file)
	layers = []
	for layer in project.layers:
		image = Image.fromarray(layer.image)
		layers.append(Layer(layer.name, image, image.size, (0, 0),
		layer.opacity / 255, layer.visible, blendModeLookup(layer.blendMode, blendLookup)))
	return LayeredImage(layers, (project.width, project.height))

def saveLayer_PDN(_fileName, _layeredImage):
	""" Save a layered image as .pdn """
	Logger(FHFormatter()).logPrint("Saving PDNs is not implemented in pypdn", LogType.ERROR)
	raise NotImplementedError


#### TIFF ####
def openLayer_TIFF(file):
	""" Open a .tiff or a .tif file into a layered image """
	from PIL import Image
	project = Image.open(file)
	layers = []
	dimensions = [0, 0]
	for index in range(project.n_frames):
		# Load the correct image
		project.seek(index)
		# Update the project dimensions
		for indx, dimension in enumerate(dimensions):
			if project.size[indx] > dimension:
				dimensions[indx] = project.size[indx]
		ifd = project.ifd.named()
		# Offsets
		offsetX = 0
		offsetY = 0
		if 'XPosition' in ifd:
			offsetX = int(ifd["XPosition"][0][0] / ifd["XPosition"][0][1] * ifd['XResolution'][0][0])
		if 'YPosition' in ifd:
			offsetY = int(ifd["YPosition"][0][0] / ifd["YPosition"][0][1] * ifd['YResolution'][0][0])
		# Add the layer
		layers.append(Layer(ifd['PageName'][0], project.copy(),
		(ifd["ImageWidth"][0], ifd["ImageLength"][0]), (offsetX, offsetY), 1, True))
	project.close()
	return LayeredImage(layers, (dimensions[0], dimensions[1]))


def saveLayer_TIFF(fileName, layeredImage):
	""" Save a layered image as .tiff or .tif """
	if len(layeredImage.extractGroups()) > 0:
		Logger(FHFormatter()).logPrint("TIFFs do not support groups so extracting layers",
		LogType.WARNING)
	layers = []
	for layer in layeredImage.extractLayers():
		layers.append(rasterImageOA(layer.image, layeredImage.dimensions, layer.opacity, layer.offsets))

	layers[0].save(fileName, compression=None, save_all=True, append_images=layers[1:])
