"""Do file io - LAYERED(C)."""

from __future__ import annotations

import io
import json
import zipfile
from typing import Any
from zipfile import ZipFile

from blendmodes.blend import BlendType
from PIL import Image

from layeredimage.io.common import blendModeLookup
from layeredimage.layeredimage import LayeredImage
from layeredimage.layergroup import Group, Layer


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
						name=layerOrGroup["name"],
						layers=layers,
						dimensions=layerOrGroup["dimensions"],
						offsets=layerOrGroup["offsets"],
						opacity=layerOrGroup["opacity"],
						visible=layerOrGroup["visible"],
						blendmode=blendModeLookup(layerOrGroup["blendmode"], blendLookup),
					)
				)
		return LayeredImage(layersAndGroups, stack["dimensions"])


def grabLayer_LAYERED(
	zipFile: ZipFile, layer: dict[str, Any], blendLookup: dict[str, Any]
) -> Layer:
	"""Grab an image from .layered."""
	with zipFile.open(f'data/{layer["name"]}.png') as layerImage:
		image = Image.open(layerImage).convert("RGBA")
	return Layer(
		name=layer["name"],
		image=image,
		dimensions=layer["dimensions"],
		offsets=layer["offsets"],
		opacity=layer["opacity"],
		visible=layer["visible"],
		blendmode=blendModeLookup(layer["blendmode"], blendLookup),
	)


def saveLayer_LAYERED(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .layered."""
	_saveLayer_LAYERED(fileName, layeredImage)


def _saveLayer_LAYERED(
	fileName: str, layeredImage: LayeredImage, *, compressed: bool = False
) -> None:
	"""Save a layered image as .layered."""
	with zipfile.ZipFile(
		fileName, "w", compression=(zipfile.ZIP_DEFLATED if compressed else zipfile.ZIP_STORED)
	) as layered:
		layered.writestr(
			"stack.json", json.dumps(layeredImage.json(), indent=(None if compressed else True))
		)
		for layer in layeredImage.layers:
			writeImage_LAYERED(
				layer.image, layered, f"data/{layer.name}.png", compressed=compressed
			)
		compositeImage = layeredImage.getFlattenLayers()
		thumbnail = compositeImage.copy()
		thumbnail.thumbnail((256, 256))
		imageLookup = {"composite": compositeImage, "thumbnail": thumbnail}
		for imageName, imageData in imageLookup.items():
			writeImage_LAYERED(imageData, layered, f"{imageName}.png", compressed=compressed)


def writeImage_LAYERED(
	image: Image.Image, zipFile: ZipFile, path: str, *, compressed: bool = False
) -> None:
	"""Write an image to the archive."""
	imgByteArr = io.BytesIO()
	imageCopy = image.copy()
	paletteSize = 256
	if compressed and len(set(imageCopy.getcolors(maxcolors=paletteSize**3))) < paletteSize:
		imageCopy = imageCopy.quantize(colors=paletteSize, method=2, kmeans=1)
	imageCopy.save(imgByteArr, format="PNG", optimize=compressed)
	imgByteArr.seek(0)
	zipFile.writestr(path, imgByteArr.read())


## LAYEREDC ##
def openLayer_LAYEREDC(file: str) -> LayeredImage:
	"""Open a .layeredc file into a layered image."""
	return openLayer_LAYERED(file)


def saveLayer_LAYEREDC(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layeredc image as .layered."""
	_saveLayer_LAYERED(fileName, layeredImage, compressed=True)
