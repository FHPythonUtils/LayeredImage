"""Do file io - Common Operations for file readers/writers."""
from __future__ import annotations

from typing import Any

from blendmodes.imagetools import renderWAlphaOffset
from PIL.Image import Image

from ..blend import BlendType
from ..layeredimage import LayeredImage


def blendModeLookup(
	blendmode: Any, blendLookup: dict[Any, Any], default: Any = BlendType.NORMAL
) -> BlendType:
	"""Get the blendmode from a lookup table."""
	if blendmode not in blendLookup:
		print(f"WARNING: {blendmode} is not currently supported!")
		return default
	return blendLookup[blendmode]


def expandLayersToCanvas(layeredImage: LayeredImage, imageFormat: str) -> list[Image]:
	"""Return layers and throw a warning if the image has groups."""
	if len(layeredImage.extractGroups()) > 0:
		print(f"WARNING: {imageFormat}s do not " "support groups so extracting layers")
	layers = []
	for layer in layeredImage.extractLayers():
		layers.append(
			renderWAlphaOffset(layer.image, layeredImage.dimensions, layer.opacity, layer.offsets)
		)
	return layers
