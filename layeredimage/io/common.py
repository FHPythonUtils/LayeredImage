"""Do file io - Common Operations for file readers/writers."""
from __future__ import annotations

from typing import Any

from blendmodes.blend import BlendType, blendLayers
from loguru import logger
from PIL import Image

from layeredimage.layeredimage import LayeredImage


def blendModeLookup(
	blendmode: Any,
	blendLookup: dict[Any, Any],
	default: BlendType | tuple[str, ...] = BlendType.NORMAL,
) -> BlendType:
	"""Get the blendmode from a lookup table."""
	if blendmode not in blendLookup:
		logger.warning("Blendmode is not currently supported!", extra={"blendmode": blendmode})
		return default
	return blendLookup[blendmode]


def expandLayersToCanvas(layeredImage: LayeredImage, imageFormat: str) -> list[Image.Image]:
	"""Return layers and throw a warning if the image has groups."""
	if len(layeredImage.extractGroups()) > 0:
		logger.warning(
			"This image format does not support groups so extracting layers",
			extra={"imageFormat": imageFormat},
		)
	return [
		blendLayers(
			background=Image.new("RGBA", layeredImage.dimensions, (0, 0, 0, 0)),
			foreground=layer.image,
			blendType=layer.blendmode,
			opacity=layer.opacity,
			offsets=layer.offsets,
		)
		for layer in layeredImage.extractLayers()
	]
