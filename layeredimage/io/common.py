"""Do file io - Common Operations for file readers/writers."""
from __future__ import annotations

from typing import Any

from metprint import FHFormatter, Logger, LogType

from ..blend import BlendType
from ..layeredimage import LayeredImage, rasterImageOA


def blendModeLookup(blendmode: Any,
blendLookup: dict[Any, Any],
default: Any = BlendType.NORMAL) -> BlendType:
	"""Get the blendmode from a lookup table."""
	if blendmode not in blendLookup:
		Logger(FHFormatter(
		)).logPrint(str(blendmode) + " is not currently supported!", LogType.WARNING)
		return default
	return blendLookup[blendmode]


def getRasterLayers(layeredImage: LayeredImage, imageFormat: str):
	"""Return layers and throw a warning if the image has groups."""
	if len(layeredImage.extractGroups()) > 0:
		Logger(FHFormatter(
		)).logPrint(imageFormat + "s do not "
		"support groups so extracting layers",
		LogType.WARNING)
	layers = []
	for layer in layeredImage.extractLayers():
		layers.append(
		rasterImageOA(layer.image,
		layeredImage.dimensions,
		layer.opacity,
		layer.offsets))
	return layers
