"""Provide blending functions and types

Adapted from https://github.com/addisonElliott/pypdn/blob/master/pypdn/reader.py
MIT License Copyright (c) 2020 FredHappyface
MIT License Copyright (c) 2018 Addison Elliott
"""

from enum import Enum
import warnings
import numpy as np
import skimage
from PIL import Image

class BlendType(Enum):
	"""Specify supported blend types
	"""
	NORMAL = 0
	MULTIPLY = 1
	ADDITIVE = 2
	COLOURBURN = 3
	COLOURDODGE = 4
	REFLECT = 5
	GLOW = 6
	OVERLAY = 7
	DIFFERENCE = 8
	NEGATION = 9
	LIGHTEN = 10
	DARKEN = 11
	SCREEN = 12
	XOR = 13


def blend(background, foreground, blendType):
	"""blend pixels

	Args:
		background (float): background px
		foreground (float): foreground px
		blendType (BlendType): the blend type

	Returns:
		[type]: [description]
	"""
	if blendType == BlendType.MULTIPLY:
		return background * foreground
	if blendType == BlendType.ADDITIVE:
		return np.minimum(background + foreground, 1.0)
	if blendType == BlendType.COLOURBURN:
		with np.errstate(divide='ignore'):
			return np.where(foreground != 0.0, np.maximum(1.0 - ((1.0 - background) / foreground), 0.0), 0.0)
	if blendType == BlendType.COLOURDODGE:
		with np.errstate(divide='ignore'):
			return np.where(foreground != 1.0, np.minimum(background / (1.0 - foreground), 1.0), 1.0)
	if blendType == BlendType.REFLECT:
		with np.errstate(divide='ignore'):
			return np.where(foreground != 1.0, np.minimum((background ** 2) / (1.0 - foreground), 1.0), 1.0)
	if blendType == BlendType.GLOW:
		with np.errstate(divide='ignore'):
			return np.where(background != 1.0, np.minimum((foreground ** 2) / (1.0 - background), 1.0), 1.0)
	if blendType == BlendType.OVERLAY:
		return np.where(background < 0.5, 2 * background * foreground, 1.0 - (2 *
		(1.0 - background) * (1.0 - foreground)))
	if blendType == BlendType.DIFFERENCE:
		return np.abs(background - foreground)
	if blendType == BlendType.NEGATION:
		return 1.0 - np.abs(1.0 - background - foreground)
	if blendType == BlendType.LIGHTEN:
		return np.maximum(background, foreground)
	if blendType == BlendType.DARKEN:
		return np.minimum(background, foreground)
	if blendType == BlendType.SCREEN:
		return background + foreground - background * foreground
	if blendType == BlendType.XOR:
		# XOR requires int values so convert to uint8
		with warnings.catch_warnings():
			warnings.simplefilter('ignore')
			return skimage.img_as_float(skimage.img_as_ubyte(background) ^ skimage.img_as_ubyte(foreground))
	# BlendType.NORMAL
	return foreground


def blendLayers(background, foreground, blendType):
	"""Blend layers using numpy array

	Args:
		background (numpy.array): background layer
		foreground (numpy.array): foreground layer
		blendType (BlendType): The blendtype

	Returns:
		numpy.array: combined image
	"""
	# Convert the PIL.Image to a numpy array
	foreground = skimage.img_as_float(np.array(foreground))
	background = skimage.img_as_float(np.array(background))

	# Get the alpha from the layers
	backgroundAlpha = background[:, :, 3]
	foregroundAlpha = foreground[:, :, 3]
	combinedAlpha = backgroundAlpha * foregroundAlpha

	# Get the colour from the layers
	backgroundColor = background[:, :, 0:3]
	foregroundColor = foreground[:, :, 0:3]

	# Get the colours and the alpha for the new image
	colorComponents = (backgroundAlpha - combinedAlpha)[:, :,
	None] * backgroundColor + (foregroundAlpha - combinedAlpha)[:, :,
	None] * foregroundColor + combinedAlpha[:, :, None] * blend(backgroundColor,
	foregroundColor, blendType)
	alphaComponent = backgroundAlpha + foregroundAlpha - combinedAlpha

	return Image.fromarray(skimage.img_as_ubyte(np.dstack((colorComponents, alphaComponent))))
