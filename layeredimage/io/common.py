"""Do file io - Common Operations for file readers/writers."""
from __future__ import annotations

from typing import Any

from blendmodes.imagetools import renderWAlphaOffset
from loguru import logger
from PIL.Image import Image

from layeredimage.blend import BlendType
from layeredimage.layeredimage import LayeredImage


def blendModeLookup(
	blendmode: Any, blendLookup: dict[Any, Any], default: Any = BlendType.NORMAL
) -> BlendType:
	"""Get the blendmode from a lookup table."""
	if blendmode not in blendLookup:
		logger.warning("Blendmode is not currently supported!", extra={"blendmode": blendmode})
		return default
	return blendLookup[blendmode]


def expandLayersToCanvas(layeredImage: LayeredImage, imageFormat: str) -> list[Image]:
	"""Return layers and throw a warning if the image has groups."""
	if len(layeredImage.extractGroups()) > 0:
		logger.warning(
			"This image format does not support groups so extracting layers",
			extra={"imageFormat": imageFormat},
		)
	layers = []
	for layer in layeredImage.extractLayers():
		layers.append(
			renderWAlphaOffset(layer.image, layeredImage.dimensions, layer.opacity, layer.offsets)
		)
	return layers
