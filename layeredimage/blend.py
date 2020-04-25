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
	SOFTLIGHT = 14
	HARDLIGHT = 15

def normal(_background, foreground):
	""" BlendType.NORMAL """
	return foreground

def multiply(background, foreground):
	""" BlendType.MULTIPLY """
	return background * foreground

def additive(background, foreground):
	""" BlendType.ADDITIVE """
	return np.minimum(background + foreground, 1.0)

def colourburn(background, foreground):
	""" BlendType.COLOURBURN """
	with np.errstate(divide='ignore'):
		return np.where(foreground != 0.0, np.maximum(1.0 - ((1.0 -
		background) / foreground), 0.0), 0.0)

def colourdodge(background, foreground):
	""" BlendType.COLOURDODGE """
	with np.errstate(divide='ignore'):
		return np.where(foreground != 1.0, np.minimum(background / (1.0 -
		foreground), 1.0), 1.0)

def reflect(background, foreground):
	""" BlendType.REFLECT """
	with np.errstate(divide='ignore'):
		return np.where(foreground != 1.0, np.minimum((background ** 2) / (1.0
		- foreground), 1.0), 1.0)

def glow(background, foreground):
	""" BlendType.GLOW """
	with np.errstate(divide='ignore'):
		return np.where(background != 1.0, np.minimum((foreground ** 2) / (1.0
		- background), 1.0), 1.0)

def overlay(background, foreground):
	""" BlendType.OVERLAY """
	return np.where(background < 0.5, 2 * background * foreground, 1.0 - (2 *
		(1.0 - background) * (1.0 - foreground)))

def difference(background, foreground):
	""" BlendType.DIFFERENCE """
	return np.abs(background - foreground)

def negation(background, foreground):
	""" BlendType.NEGATION """
	return 1.0 - np.abs(1.0 - background - foreground)

def lighten(background, foreground):
	""" BlendType.LIGHTEN """
	return np.maximum(background, foreground)

def darken(background, foreground):
	""" BlendType.DARKEN """
	return np.minimum(background, foreground)

def screen(background, foreground):
	""" BlendType.SCREEN """
	return background + foreground - background * foreground

def xor(background, foreground):
	""" BlendType.XOR """
	# XOR requires int values so convert to uint8
	with warnings.catch_warnings():
		warnings.simplefilter('ignore')
		return skimage.img_as_float(skimage.img_as_ubyte(background) ^
		skimage.img_as_ubyte(foreground))

def softlight(background, foreground):
	""" BlendType.SOFTLIGHT """
	return (1.0 - background) * background * foreground + background * (1.0 -
		(1.0 - background) * (1.0 - foreground))

def hardlight(background, foreground):
	""" BlendType.HARDLIGHT """
	return np.where(foreground > 0.5, np.minimum(background * 2 * foreground, 1.0),
		np.minimum(1.0 - ((1.0 - background) * (1.0 - (foreground - 0.5) * 2.0)),
		1.0))

def blend(background, foreground, blendType):
	"""blend pixels

	Args:
		background (np.array): background
		foreground (np.array): foreground
		blendType (BlendType): the blend type

	Returns:
		np.array: new array representing the image

	background, foreground and the return are in the form

	[[[0. 0. 0.]
	[0. 0. 0.]
	[0. 0. 0.]
	...
	[0. 0. 0.]
	[0. 0. 0.]
	[0. 0. 0.]]

	...

	[[0. 0. 0.]
	[0. 0. 0.]
	[0. 0. 0.]
	...
	[0. 0. 0.]
	[0. 0. 0.]
	[0. 0. 0.]]]
	"""
	blendLookup = {BlendType.NORMAL: normal, BlendType.MULTIPLY: multiply,
	BlendType.COLOURBURN: colourburn,	BlendType.COLOURDODGE: colourdodge,
	BlendType.REFLECT: reflect,	BlendType.OVERLAY: overlay,
	BlendType.DIFFERENCE: difference,	BlendType.LIGHTEN: lighten,
	BlendType.DARKEN: darken, BlendType.SCREEN: screen,
	BlendType.SOFTLIGHT: softlight, BlendType.HARDLIGHT: hardlight}

	if blendType not in blendLookup:
		return normal(background, foreground)
	return blendLookup[blendType](background, foreground)


def blendLayers(background, foreground, blendType, opacity):
	"""Blend layers using numpy array

	Args:
		background (PIL.Image): background layer
		foreground (PIL.Image): foreground layer
		blendType (BlendType): The blendtype
		opacity (float): The opacity of the foreground image

	Returns:
		PIL.Image: combined image
	"""
	# Convert the PIL.Image to a numpy array
	foreground = skimage.img_as_float(np.array(foreground))
	background = skimage.img_as_float(np.array(background))

	# Get the alpha from the layers
	backgroundAlpha = background[:, :, 3]
	foregroundAlpha = foreground[:, :, 3] * opacity
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
