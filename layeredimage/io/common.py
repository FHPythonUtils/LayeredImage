"""Do file io - Common Operations for file readers/writers."""

from __future__ import annotations

from typing import Any

import numpy as np
from blendmodes.blend import BlendType
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
		expandLayer(
			dimensions=layeredImage.dimensions,
			foreground=layer.image,
			opacity=layer.opacity,
			offsets=layer.offsets,
		)
		for layer in layeredImage.extractLayers()
	]


def expandLayer(
	dimensions: tuple[int, int],
	foreground: np.ndarray | Image.Image,
	opacity: float = 1.0,
	offsets: tuple[int, int] = (0, 0),
) -> Image.Image:
	"""
	Args:
	----
		foreground (np.ndarray | Image.Image): The foreground layer (must be the same size as the background).
		opacity (float, optional): The opacity of the foreground image. Defaults to 1.0.
		offsets (Tuple[int, int], optional): Offsets for the foreground layer. Defaults to (0, 0).

	Returns:
	-------
		Image.Image: The image.

	"""
	# Convert the Image.Image to a numpy array if required
	if isinstance(foreground, Image.Image):
		foreground = np.array(foreground.convert("RGBA"))

	# do any offset shifting first
	if offsets[0] > 0:
		foreground = np.hstack(
			(np.zeros((foreground.shape[0], offsets[0], 4), dtype=np.float64), foreground)
		)
	elif offsets[0] < 0:
		if offsets[0] > -1 * foreground.shape[1]:
			foreground = foreground[:, -1 * offsets[0] :, :]
		else:
			# offset offscreen completely, there is nothing left
			return Image.fromarray(np.zeros(dimensions, dtype=np.uint8))
	if offsets[1] > 0:
		foreground = np.vstack(
			(np.zeros((offsets[1], foreground.shape[1], 4), dtype=np.float64), foreground)
		)
	elif offsets[1] < 0:
		if offsets[1] > -1 * foreground.shape[0]:
			foreground = foreground[-1 * offsets[1] :, :, :]
		else:
			# offset offscreen completely, there is nothing left
			return Image.fromarray(np.zeros(dimensions, dtype=np.uint8))

	# resize array to fill small images with zeros
	if foreground.shape[0] < dimensions[0]:
		foreground = np.vstack(
			(
				foreground,
				np.zeros(
					(dimensions[0] - foreground.shape[0], foreground.shape[1], 4),
					dtype=np.float64,
				),
			)
		)
	if foreground.shape[1] < dimensions[1]:
		foreground = np.hstack(
			(
				foreground,
				np.zeros(
					(foreground.shape[0], dimensions[1] - foreground.shape[1], 4),
					dtype=np.float64,
				),
			)
		)

	# crop the source if the backdrop is smaller
	foreground = foreground[: dimensions[0], : dimensions[1], :]

	upper_norm = foreground

	upper_alpha = upper_norm[:, :, 3] * opacity
	upper_rgb = upper_norm[:, :, :3]

	arr = np.nan_to_num(np.dstack((upper_rgb, upper_alpha)), copy=False)
	return Image.fromarray(np.uint8(np.around(arr, 0)))
