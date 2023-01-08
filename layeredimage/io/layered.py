"""Do file io - LAYERED(C)."""
from __future__ import annotations

import io
import json
import zipfile
from typing import Any
from zipfile import ZipFile

from PIL import Image

from ..blend import BlendType
from ..layeredimage import LayeredImage
from ..layergroup import Group, Layer
from .common import blendModeLookup

# pylint: disable=invalid-name


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
		"SRCATOP": BlendType.SRCATOP,
	}
	layersAndGroups = []
	with zipfile.ZipFile(file, "r") as layered:
		with layered.open("stack.json") as stackJson:
			stack = json.load(stackJson)
		# Iterate through the layers and groups
		for layerOrGroup in stack["layersAndGroups"]:
			if layerOrGroup["type"] == "LAYER":
				layersAndGroups.append(grabLayer_LAYERED(layered, layerOrGroup, blendLookup))
			else:
				# If its a group grab the layers
				layers = [
					grabLayer_LAYERED(layered, layer, blendLookup)
					for layer in layerOrGroup["layers"]
				]
				layersAndGroups.append(
					Group(
						layerOrGroup["name"],
						layers,
						layerOrGroup["dimensions"],
						layerOrGroup["offsets"],
						layerOrGroup["opacity"],
						layerOrGroup["visible"],
						blendModeLookup(layerOrGroup["blendmode"], blendLookup),
					)
				)
		return LayeredImage(layersAndGroups, stack["dimensions"])


def grabLayer_LAYERED(zipFile: ZipFile, layer: dict[str, Any], blendLookup: dict[str, Any]):
	"""Grab an image from .layered."""
	with zipFile.open("data/" + layer["name"] + ".png") as layerImage:
		image = Image.open(layerImage).convert("RGBA")
	return Layer(
		layer["name"],
		image,
		layer["dimensions"],
		layer["offsets"],
		layer["opacity"],
		layer["visible"],
		blendModeLookup(layer["blendmode"], blendLookup),
	)


def saveLayer_LAYERED(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .layered."""
	_saveLayer_LAYERED(fileName, layeredImage)


def _saveLayer_LAYERED(fileName: str, layeredImage: LayeredImage, compressed: bool = False) -> None:
	"""Save a layered image as .layered."""
	with zipfile.ZipFile(
		fileName, "w", compression=(zipfile.ZIP_DEFLATED if compressed else zipfile.ZIP_STORED)
	) as layered:
		layered.writestr(
			"stack.json", json.dumps(layeredImage.json(), indent=(None if compressed else True))
		)
		for layer in layeredImage.layers:
			writeImage_LAYERED(layer.image, layered, "data/" + layer.name + ".png", compressed)
		compositeImage = layeredImage.getFlattenLayers()
		thumbnail = compositeImage.copy()
		thumbnail.thumbnail((256, 256))
		imageLookup = {"composite": compositeImage, "thumbnail": thumbnail}
		for imageName, imageData in imageLookup.items():
			writeImage_LAYERED(imageData, layered, imageName + ".png", compressed)


def writeImage_LAYERED(image: Image.Image, zipFile: ZipFile, path: str, compressed: bool = False):
	"""Write an image to the archive."""
	imgByteArr = io.BytesIO()
	imageCopy = image.copy()
	if compressed and len(set(imageCopy.getcolors(maxcolors=256**3))) < 256:
		imageCopy = imageCopy.quantize(colors=256, method=2, kmeans=1)
	imageCopy.save(imgByteArr, format="PNG", optimize=compressed)
	imgByteArr.seek(0)
	zipFile.writestr(path, imgByteArr.read())


## LAYEREDC ##
def openLayer_LAYEREDC(file: str) -> LayeredImage:
	"""Open a .layeredc file into a layered image."""
	return openLayer_LAYERED(file)


def saveLayer_LAYEREDC(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layeredc image as .layered."""
	_saveLayer_LAYERED(fileName, layeredImage, True)
