"""Do file io."""
from __future__ import annotations

import io
import json
import zipfile
from os.path import exists
from typing import Any
from zipfile import ZipFile

from metprint import FHFormatter, Logger, LogType
from PIL import Image

from layeredimage.blend import BlendType
from layeredimage.layeredimage import LayeredImage, rasterImageOA
from layeredimage.layergroup import Group, Layer

# To avoid throwing import errors for the sake of it, specialised imports are
# to be scoped to the function
# pylint: disable=import-outside-toplevel
# pylint: disable=invalid-name


def extNotRecognised(fileName: str):
	"""Output the file extension not recognised error."""
	exts = [
	"ora",
	"psd",
	"xcf",
	"pdn",
	"tif",
	"tiff",
	"webp",
	"gif",
	"lsr",
	"layered",
	"layeredc"]
	Logger(FHFormatter()).logPrint(
	"File extension is not recognised for file: " + fileName + "! Must be "
	"one of \"" + ", \"".join(exts) + "\"",
	LogType.ERROR)


def openLayerImage(file: str) -> LayeredImage:
	"""Open a layer image file into a layer image object.

	Args:
		file (str): path/ filename

	Returns:
		LayeredImage: a layered image object
	"""
	functionMap = {
	"ora": openLayer_ORA,
	"psd": openLayer_PSD,
	"xcf": openLayer_XCF,
	"pdn": openLayer_PDN,
	"tif": openLayer_TIFF,
	"tiff": openLayer_TIFF,
	"webp": openLayer_WEBP,
	"gif": openLayer_GIF,
	"lsr": openLayer_LSR,
	"layered": openLayer_LAYERED,
	"layeredc": openLayer_LAYEREDC}
	if not exists(file):
		Logger(FHFormatter()).logPrint(file + " does not exist", LogType.ERROR)
		raise FileExistsError
	fileExt = file.split(".")[-1].lower()
	if fileExt not in functionMap:
		extNotRecognised(file)
		raise ValueError
	return functionMap[fileExt](file)


def saveLayerImage(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image to a file.

	Args:
		fileName (str): path/ filename
		layeredImage (LayeredImage): the layered image to save
	"""
	functionMap = {
	"ora": saveLayer_ORA,
	"psd": saveLayer_PSD,
	"xcf": saveLayer_XCF,
	"pdn": saveLayer_PDN,
	"tif": saveLayer_TIFF,
	"tiff": saveLayer_TIFF,
	"webp": saveLayer_WEBP,
	"gif": saveLayer_GIF,
	"lsr": saveLayer_LSR,
	"layered": saveLayer_LAYERED,
	"layeredc": saveLayer_LAYEREDC}
	fileExt = fileName.split(".")[-1].lower()
	if fileExt not in functionMap:
		extNotRecognised(fileName)
		raise ValueError
	return functionMap[fileExt](fileName, layeredImage)


def exportFlatImage(fileName: str, layeredImage: LayeredImage) -> None:
	"""Export the layered image to a unilayer image file."""
	layeredImage.getFlattenLayers().save(fileName)


def blendModeLookup(blendmode: Any,
blendLookup: dict[Any, Any],
default: Any = BlendType.NORMAL) -> BlendType:
	"""Get the blendmode from a lookup table."""
	if blendmode not in blendLookup:
		Logger(FHFormatter(
		)).logPrint(str(blendmode) + " is not currently supported!", LogType.WARNING)
		return default
	return blendLookup[blendmode]


#### ORA ####
def openLayer_ORA(file: str) -> LayeredImage:
	"""Open an .ora file into a layered image."""
	from pyora import TYPE_LAYER, Project

	# Not implemented color luminosity hue saturation
	blendLookup = {
	"svg:src-over": BlendType.NORMAL,
	"svg:multiply": BlendType.MULTIPLY,
	"svg:color-burn": BlendType.COLOURBURN,
	"svg:color-dodge": BlendType.COLOURDODGE,
	"svg:": BlendType.REFLECT,
	"svg:overlay": BlendType.OVERLAY,
	"svg:difference": BlendType.DIFFERENCE,
	"svg:lighten": BlendType.LIGHTEN,
	"svg:darken": BlendType.DARKEN,
	"svg:screen": BlendType.SCREEN,
	"svg:hard-light": BlendType.HARDLIGHT,
	"svg:soft-light": BlendType.SOFTLIGHT,
	"svg:hue": BlendType.HUE,
	"svg:saturation": BlendType.SATURATION,
	"svg:color": BlendType.COLOUR,
	"svg:luminosity": BlendType.LUMINOSITY,
	"svg:plus": BlendType.ADDITIVE,
	"svg:dst-in": BlendType.DESTIN,
	"svg:dst-out": BlendType.DESTOUT,
	"svg:dst-atop": BlendType.DESTATOP,
	"svg:src-atop": BlendType.SRCATOP}
	layersAndGroups = []
	project = Project.load(file)
	for layerOrGroup in project.children[::-1]:
		if layerOrGroup.type == TYPE_LAYER:
			layersAndGroups.append(
			Layer(layerOrGroup.name,
			layerOrGroup.get_image_data(True),
			layerOrGroup.dimensions,
			layerOrGroup.offsets,
			layerOrGroup.opacity,
			layerOrGroup.visible,
			blendModeLookup(layerOrGroup.composite_op, blendLookup)))
		else:
			layers = []
			for layer in list(layerOrGroup.children)[::-1]:
				layers.append(
				Layer(layer.name,
				layer.get_image_data(True),
				layer.dimensions,
				layer.offsets,
				layer.opacity,
				layer.visible,
				blendModeLookup(layerOrGroup.composite_op, blendLookup)))
			layersAndGroups.append(
			Group(layerOrGroup.name,
			layers,
			project.dimensions,
			layerOrGroup.offsets,
			layerOrGroup.opacity,
			layerOrGroup.visible,
			blendModeLookup(layerOrGroup.composite_op, blendLookup)))
	return LayeredImage(layersAndGroups, project.dimensions)


def saveLayer_ORA(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .ora."""
	from pyora import Project
	blendLookup = {
	BlendType.NORMAL: "svg:src-over",
	BlendType.MULTIPLY: "svg:multiply",
	BlendType.COLOURBURN: "svg:color-burn",
	BlendType.COLOURDODGE: "svg:color-dodge",
	BlendType.REFLECT: "svg:",
	BlendType.OVERLAY: "svg:overlay",
	BlendType.DIFFERENCE: "svg:difference",
	BlendType.LIGHTEN: "svg:lighten",
	BlendType.DARKEN: "svg:darken",
	BlendType.SCREEN: "svg:screen",
	BlendType.SOFTLIGHT: "svg:soft-light",
	BlendType.HARDLIGHT: "svg:hard-light",
	BlendType.HUE: "svg:hue",
	BlendType.SATURATION: "svg:saturation",
	BlendType.COLOUR: "svg:color",
	BlendType.LUMINOSITY: "svg:luminosity",
	BlendType.ADDITIVE: "svg:plus",
	BlendType.DESTIN: "svg:dst-in",
	BlendType.DESTOUT: "svg:dst-out",
	BlendType.DESTATOP: "svg:dst-atop",
	BlendType.SRCATOP: "svg:src-atop"}
	project = Project.new(layeredImage.dimensions[0], layeredImage.dimensions[1])
	for layerOrGroup in layeredImage.layersAndGroups:
		if isinstance(layerOrGroup, Layer):
			project = addLayer_ORA(project, layerOrGroup, blendLookup)
		else:
			group = project.add_group(
			layerOrGroup.name,
			offsets=layerOrGroup.offsets,
			opacity=layerOrGroup.opacity,
			visible=layerOrGroup.visible,
			composite_op=blendModeLookup(layerOrGroup.blendmode,
			blendLookup,
			"svg:src-over"))
			for layer in layerOrGroup.layers:
				group = addLayer_ORA(group, layer, blendLookup)
	project.save(fileName)


def addLayer_ORA(project, layer, blendLookup):
	"""Update the project with a shiny new layer."""
	project.add_layer(
	layer.image,
	layer.name,
	offsets=layer.offsets,
	opacity=layer.opacity,
	visible=layer.visible,
	composite_op=blendModeLookup(layer.blendmode, blendLookup, "svg:src-over"))
	return project


#### PSD ####
def openLayer_PSD(file: str) -> LayeredImage:
	"""Open a .psd file into a layered image."""
	from psdtoolsx import PSDImage
	from psdtoolsx.constants import BlendMode as psdB
	blendLookup = {
	psdB.NORMAL: BlendType.NORMAL,
	psdB.MULTIPLY: BlendType.MULTIPLY,
	psdB.COLOR_BURN: BlendType.COLOURBURN,
	psdB.COLOR_DODGE: BlendType.COLOURDODGE,
	psdB.OVERLAY: BlendType.OVERLAY,
	psdB.DIFFERENCE: BlendType.DIFFERENCE,
	psdB.SUBTRACT: BlendType.NEGATION,
	psdB.LIGHTEN: BlendType.LIGHTEN,
	psdB.DARKEN: BlendType.DARKEN,
	psdB.SCREEN: BlendType.SCREEN,
	psdB.SOFT_LIGHT: BlendType.SOFTLIGHT,
	psdB.HARD_LIGHT: BlendType.HARDLIGHT,
	psdB.EXCLUSION: BlendType.EXCLUSION,
	psdB.HUE: BlendType.HUE,
	psdB.SATURATION: BlendType.SATURATION,
	psdB.COLOR: BlendType.COLOUR,
	psdB.LUMINOSITY: BlendType.LUMINOSITY,
	psdB.DIVIDE: BlendType.DIVIDE,
	psdB.PIN_LIGHT: BlendType.PINLIGHT,
	psdB.VIVID_LIGHT: BlendType.VIVIDLIGHT}
	layersAndGroups = []
	project = PSDImage.open(file)
	for layerOrGroup in project:
		if layerOrGroup.is_group():
			layers = []
			for layer in layerOrGroup:
				layers.append(
				Layer(layer.name,
				layer.topil(), (layer.width, layer.height),
				(layer.left - layerOrGroup.left, layer.top - layerOrGroup.top),
				layer.opacity / 255,
				layer.visible,
				blendModeLookup(layer.blend_mode, blendLookup)))
			layersAndGroups.append(
			Group(layerOrGroup.name,
			layers, (layerOrGroup.width, layerOrGroup.height),
			(layerOrGroup.left, layerOrGroup.top),
			layerOrGroup.opacity / 255,
			layerOrGroup.visible,
			blendModeLookup(layerOrGroup.blend_mode, blendLookup)))
		else:
			layersAndGroups.append(
			Layer(layerOrGroup.name,
			layerOrGroup.topil(), (layerOrGroup.width, layerOrGroup.height),
			(layerOrGroup.left, layerOrGroup.top),
			layerOrGroup.opacity / 255,
			layerOrGroup.visible,
			blendModeLookup(layerOrGroup.blend_mode, blendLookup)))
	return LayeredImage(layersAndGroups, (project.width, project.height))


def saveLayer_PSD(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .psd."""
	Logger(FHFormatter()).logPrint("Saving PSDs is not implemented in psdtoolsx",
	LogType.ERROR)
	raise NotImplementedError


#### XCF ####
def openLayer_XCF(file: str) -> LayeredImage:
	"""Open an .xcf file into a layered image."""
	from gimpformats.gimpXcfDocument import GimpDocument
	blendLookup = {
	0: BlendType.NORMAL,
	3: BlendType.MULTIPLY,
	4: BlendType.SCREEN,
	5: BlendType.OVERLAY,
	6: BlendType.DIFFERENCE,
	7: BlendType.ADDITIVE,
	8: BlendType.NEGATION,
	9: BlendType.DARKEN,
	10: BlendType.LIGHTEN,
	11: BlendType.HUE,
	12: BlendType.SATURATION,
	13: BlendType.COLOUR,
	14: BlendType.LUMINOSITY,
	15: BlendType.DIVIDE,
	16: BlendType.COLOURDODGE,
	17: BlendType.COLOURBURN,
	18: BlendType.HARDLIGHT,
	19: BlendType.SOFTLIGHT,
	20: BlendType.GRAINEXTRACT,
	21: BlendType.GRAINMERGE,
	23: BlendType.OVERLAY,
	24: BlendType.HUE,
	25: BlendType.SATURATION,
	26: BlendType.COLOUR,
	27: BlendType.LUMINOSITY,
	28: BlendType.NORMAL,
	30: BlendType.MULTIPLY,
	31: BlendType.SCREEN,
	32: BlendType.DIFFERENCE,
	33: BlendType.ADDITIVE,
	34: BlendType.NEGATION,
	35: BlendType.DARKEN,
	36: BlendType.LIGHTEN,
	37: BlendType.HUE,
	38: BlendType.SATURATION,
	39: BlendType.COLOUR,
	40: BlendType.LUMINOSITY,
	41: BlendType.DIVIDE,
	42: BlendType.COLOURDODGE,
	43: BlendType.COLOURBURN,
	44: BlendType.HARDLIGHT,
	45: BlendType.SOFTLIGHT,
	46: BlendType.GRAINEXTRACT,
	47: BlendType.GRAINMERGE,
	48: BlendType.VIVIDLIGHT,
	49: BlendType.PINLIGHT,
	52: BlendType.EXCLUSION}
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
				groupLayers[groupIndex].append(
				Layer(layer.name,
				layer.image, (layer.width, layer.height),
				(layer.xOffset - layerOrGroup.xOffset,
				layer.yOffset - layerOrGroup.yOffset),
				layer.opacity,
				layer.visible,
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
			layersAndGroups.append(
			Group(layerOrGroup.name,
			groupLayers[groupIndex][::-1], (layerOrGroup.width, layerOrGroup.height),
			(layerOrGroup.xOffset, layerOrGroup.yOffset),
			layerOrGroup.opacity,
			layerOrGroup.visible,
			blendModeLookup(layerOrGroup.blendMode, blendLookup)))
			groupIndex += 1
		else:
			layersAndGroups.append(
			Layer(layerOrGroup.name,
			layerOrGroup.image, (layerOrGroup.width, layerOrGroup.height),
			(layerOrGroup.xOffset, layerOrGroup.yOffset),
			layerOrGroup.opacity,
			layerOrGroup.visible,
			blendModeLookup(layerOrGroup.blendMode, blendLookup)))

	return LayeredImage(layersAndGroups, (project.width, project.height))


def saveLayer_XCF(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .xcf."""
	Logger(FHFormatter()).logPrint(
	"Saving XCFs is not implemented in gimpformats - " +
	"this is a little misleading as functions are pressent, however these are not "
	+ "functional",
	LogType.ERROR)
	raise NotImplementedError


#### PDN ####
def openLayer_PDN(file: str) -> LayeredImage:
	"""Open a .pdn file into a layered image."""
	from pypdn.reader import BlendType as PDNBlend, read
	blendLookup = {
	PDNBlend.Normal: BlendType.NORMAL,
	PDNBlend.Multiply: BlendType.MULTIPLY,
	PDNBlend.Additive: BlendType.ADDITIVE,
	PDNBlend.ColorBurn: BlendType.COLOURBURN,
	PDNBlend.ColorDodge: BlendType.COLOURDODGE,
	PDNBlend.Reflect: BlendType.REFLECT,
	PDNBlend.Glow: BlendType.GLOW,
	PDNBlend.Overlay: BlendType.OVERLAY,
	PDNBlend.Difference: BlendType.DIFFERENCE,
	PDNBlend.Negation: BlendType.NEGATION,
	PDNBlend.Lighten: BlendType.LIGHTEN,
	PDNBlend.Darken: BlendType.DARKEN,
	PDNBlend.Screen: BlendType.SCREEN,
	PDNBlend.XOR: BlendType.XOR}
	project = read(file)
	layers = []
	for layer in project.layers:
		image = Image.fromarray(layer.image)
		layers.append(
		Layer(layer.name,
		image,
		image.size, (0, 0),
		layer.opacity / 255,
		layer.visible,
		blendModeLookup(layer.blendMode, blendLookup)))
	return LayeredImage(layers, (project.width, project.height))


def saveLayer_PDN(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .pdn."""
	Logger(FHFormatter()).logPrint("Saving PDNs is not implemented in pypdn",
	LogType.ERROR)
	raise NotImplementedError


#### TIFF ####
def openLayer_TIFF(file: str) -> LayeredImage:
	"""Open a .tiff or a .tif file into a layered image."""
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
			offsetX = int(ifd["XPosition"][0][0] / ifd["XPosition"][0][1]
			* ifd['XResolution'][0][0])
		if 'YPosition' in ifd:
			offsetY = int(ifd["YPosition"][0][0] / ifd["YPosition"][0][1]
			* ifd['YResolution'][0][0])
		# Add the layer
		layers.append(
		Layer(ifd['PageName'][0],
		project.copy(), (ifd["ImageWidth"][0], ifd["ImageLength"][0]),
		(offsetX, offsetY),
		1,
		True))
	project.close()
	return LayeredImage(layers, (dimensions[0], dimensions[1]))


def saveLayer_TIFF(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .tiff or .tif."""
	layers = getRasterLayers(layeredImage, "TIFF")
	layers[0].save(fileName,
	compression=None,
	save_all=True,
	append_images=layers[1:])


## GIF ##
def openLayer_GIF(file: str) -> LayeredImage:
	"""Open a .gif file into a layered image."""
	project = Image.open(file)
	projectSize = project.size
	layers = []
	for index in range(project.n_frames):
		project.seek(index)
		layers.append(
		Layer("Frame {} ({}ms)".format(len(layers) + 1, project.info["duration"]),
		project.copy(),
		projectSize))
	project.close()
	return LayeredImage(layers, projectSize)


def saveLayer_GIF(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .gif."""
	layers = getRasterLayers(layeredImage, "GIF")
	layers[0].save(fileName, duration=100, save_all=True, append_images=layers[1:])


## WEBP ##
def openLayer_WEBP(file: str) -> LayeredImage:
	"""Open a .webp file into a layered image."""
	project = Image.open(file)
	projectSize = project.size
	layers = []
	for index in range(project.n_frames):
		project.seek(index)
		layers.append(
		Layer("Frame {}".format(len(layers) + 1), project.copy(), projectSize))
	project.close()
	return LayeredImage(layers, projectSize)


def saveLayer_WEBP(fileName: str, layeredImage: LayeredImage):
	"""Save a layered image as .webp."""
	layers = getRasterLayers(layeredImage, "WEBP")
	layers[0].save(fileName, duration=200, save_all=True, append_images=layers[1:])


def getRasterLayers(layeredImage: LayeredImage, imageFormat: str):
	"""Return layers and throw a warning if the image has groups."""
	if len(layeredImage.extractGroups()) > 0:
		Logger(FHFormatter()
								).logPrint(imageFormat + "s do not support groups so extracting layers",
		LogType.WARNING)
	layers = []
	for layer in layeredImage.extractLayers():
		layers.append(
		rasterImageOA(layer.image,
		layeredImage.dimensions,
		layer.opacity,
		layer.offsets))
	return layers


## LSR ##
def openLayer_LSR(file: str) -> LayeredImage:
	"""Open a .lsr file into a layered image."""
	import pylsr
	project = pylsr.read(file)
	groups = []
	for group in project.layers:
		groups.append(
		Group(group.name,
		[
		Layer(layer.name, layer.scaledImage(), layer.scaledImage().size)
		for layer in group.images],
		group.size, (int(group.offsets()[0]), int(group.offsets()[1]))))
	return LayeredImage(groups, project.size)


def saveLayer_LSR(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .lsr."""
	from os import sep

	import pylsr
	layers = []
	for group in layeredImage.layersAndGroups:
		if isinstance(group, Layer):
			imageData = [pylsr.LSRImageData(group.image, group.name)]
		else:
			imageData = [
			pylsr.LSRImageData(
			rasterImageOA(layer.image, group.dimensions, layer.opacity, layer.offsets),
			layer.name) for layer in group.layers]
		layers.append(
		pylsr.LSRLayer(imageData,
		group.name,
		group.dimensions,
		(group.offsets[0] + group.dimensions[0] // 2,
		group.offsets[1] + group.dimensions[1] // 2)))
	lsrImage = pylsr.LSRImage(layeredImage.dimensions,
	fileName.split(sep)[-1].replace(".lsr", ""),
	layers)
	pylsr.write(fileName, lsrImage)


## LAYERED ##
def openLayer_LAYERED(file: str) -> LayeredImage:
	"""Open a .layered file into a layered image."""
	blendLookup = {
	"NORMAL": BlendType.NORMAL,
	"MULTIPLY": BlendType.MULTIPLY,
	"ADDITIVE": BlendType.ADDITIVE,
	"COLOURBURN": BlendType.COLOURBURN,
	"COLOURDODGE": BlendType.COLOURDODGE,
	"REFLECT": BlendType.REFLECT,
	"GLOW": BlendType.GLOW,
	"OVERLAY": BlendType.OVERLAY,
	"DIFFERENCE": BlendType.DIFFERENCE,
	"NEGATION": BlendType.NEGATION,
	"LIGHTEN": BlendType.LIGHTEN,
	"DARKEN": BlendType.DARKEN,
	"SCREEN": BlendType.SCREEN,
	"XOR": BlendType.XOR,
	"SOFTLIGHT": BlendType.SOFTLIGHT,
	"HARDLIGHT": BlendType.HARDLIGHT,
	"GRAINEXTRACT": BlendType.GRAINEXTRACT,
	"GRAINMERGE": BlendType.GRAINMERGE,
	"DIVIDE": BlendType.DIVIDE,
	"HUE": BlendType.HUE,
	"SATURATION": BlendType.SATURATION,
	"COLOUR": BlendType.COLOUR,
	"LUMINOSITY": BlendType.LUMINOSITY,
	"PINLIGHT": BlendType.PINLIGHT,
	"VIVIDLIGHT": BlendType.VIVIDLIGHT,
	"EXCLUSION": BlendType.EXCLUSION,
	"DESTIN": BlendType.DESTIN,
	"DESTOUT": BlendType.DESTOUT,
	"DESTATOP": BlendType.DESTATOP,
	"SRCATOP": BlendType.SRCATOP}
	layersAndGroups = []
	with zipfile.ZipFile(file, 'r') as layered:
		stack = json.load(layered.open("stack.json"))
		# Iterate through the layers and groups
		for layerOrGroup in stack["layersAndGroups"]:
			if layerOrGroup["type"] == "LAYER":
				layersAndGroups.append(grabLayer_LAYERED(layered, layerOrGroup,
				blendLookup))
			else:
				# If its a group grab the layers
				layers = [
				grabLayer_LAYERED(layered, layer, blendLookup)
				for layer in layerOrGroup["layers"]]
				layersAndGroups.append(
				Group(layerOrGroup["name"],
				layers,
				layerOrGroup["dimensions"],
				layerOrGroup["offsets"],
				layerOrGroup["opacity"],
				layerOrGroup["visible"],
				blendModeLookup(layerOrGroup["blendmode"], blendLookup)))
		return LayeredImage(layersAndGroups, stack["dimensions"])


def grabLayer_LAYERED(zipFile: ZipFile,
layer: dict[str, Any],
blendLookup: dict[str, Any]):
	"""Grab an image from .layered."""
	with zipFile.open("data/" + layer["name"] + ".png") as layerImage:
		image = Image.open(layerImage).convert('RGBA')
	return Layer(layer["name"],
	image,
	layer["dimensions"],
	layer["offsets"],
	layer["opacity"],
	layer["visible"],
	blendModeLookup(layer["blendmode"], blendLookup))


def saveLayer_LAYERED(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .layered."""
	_saveLayer_LAYERED(fileName, layeredImage)


def _saveLayer_LAYERED(fileName: str,
layeredImage: LayeredImage,
compressed: bool = False) -> None:
	"""Save a layered image as .layered."""
	with zipfile.ZipFile(
	fileName,
	'w',
	compression=(zipfile.ZIP_DEFLATED
	if compressed else zipfile.ZIP_STORED)) as layered:
		layered.writestr(
		"stack.json",
		json.dumps(layeredImage.json(), indent=(None if compressed else True)))
		for layer in layeredImage.layers:
			writeImage_LAYERED(layer.image,
			layered,
			"data/" + layer.name + ".png",
			compressed)
		compositeImage = layeredImage.getFlattenLayers()
		thumbnail = compositeImage.copy()
		thumbnail.thumbnail((256, 256))
		imageLookup = {"composite": compositeImage, "thumbnail": thumbnail}
		for image in imageLookup:
			writeImage_LAYERED(imageLookup[image], layered, image + ".png", compressed)


def writeImage_LAYERED(image: Image.Image,
zipFile: ZipFile,
path: str,
compressed: bool = False):
	"""Write an image to the archive."""
	imgByteArr = io.BytesIO()
	imageCopy = image.copy()
	if compressed and len(set(imageCopy.getcolors(maxcolors=256**3))) < 256:
		imageCopy = imageCopy.quantize(colors=256, method=2, kmeans=1)
	imageCopy.save(imgByteArr, format='PNG', optimize=compressed)
	imgByteArr.seek(0)
	zipFile.writestr(path, imgByteArr.read())


## LAYEREDC ##
def openLayer_LAYEREDC(file: str) -> LayeredImage:
	"""Open a .layeredc file into a layered image."""
	return openLayer_LAYERED(file)


def saveLayer_LAYEREDC(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layeredc image as .layered."""
	_saveLayer_LAYERED(fileName, layeredImage, True)
