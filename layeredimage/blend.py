"""Provide blending functions.

leverage blendmodes for this
"""
from __future__ import annotations

from enum import Enum, auto

from blendmodes.blend import BlendType as bType, blendLayers as bLayers
from PIL.Image import Image


class BlendType(Enum):
	"""Specify supported blend types.

	NORMAL
	MULTIPLY
	ADDITIVE
	COLOURBURN
	COLOURDODGE
	REFLECT
	GLOW
	OVERLAY
	DIFFERENCE
	NEGATION
	LIGHTEN
	DARKEN
	SCREEN
	XOR
	SOFTLIGHT
	HARDLIGHT
	GRAINEXTRACT
	GRAINMERGE
	DIVIDE
	HUE
	SATURATION
	COLOUR
	LUMINOSITY
	PINLIGHT
	VIVIDLIGHT
	EXCLUSION
	DESTIN
	DESTOUT
	DESTATOP
	SRCATOP
	"""
	NORMAL = auto()
	MULTIPLY = auto()
	ADDITIVE = auto()
	COLOURBURN = auto()
	COLOURDODGE = auto()
	REFLECT = auto()
	GLOW = auto()
	OVERLAY = auto()
	DIFFERENCE = auto()
	NEGATION = auto()
	LIGHTEN = auto()
	DARKEN = auto()
	SCREEN = auto()
	XOR = auto()
	SOFTLIGHT = auto()
	HARDLIGHT = auto()
	GRAINEXTRACT = auto()
	GRAINMERGE = auto()
	DIVIDE = auto()
	HUE = auto()
	SATURATION = auto()
	COLOUR = auto()
	LUMINOSITY = auto()
	PINLIGHT = auto()
	VIVIDLIGHT = auto()
	EXCLUSION = auto()
	DESTIN = auto()
	DESTOUT = auto()
	DESTATOP = auto()
	SRCATOP = auto()


def blendLayers(background: Image,
foreground: Image,
blendType: BlendType,
opacity: float):
	"""Blend layers using numpy array.

	Args:
		background (PIL.Image): background layer
		foreground (PIL.Image): foreground layer
		blendType (BlendType): The blendtype
		opacity (float): The opacity of the foreground image

	Returns:
		PIL.Image: combined image
	"""
	blendTypeMap = {
	BlendType.NORMAL: bType.NORMAL,
	BlendType.MULTIPLY: bType.MULTIPLY,
	BlendType.COLOURBURN: bType.COLOURBURN,
	BlendType.COLOURDODGE: bType.COLOURDODGE,
	BlendType.REFLECT: bType.REFLECT,
	BlendType.OVERLAY: bType.OVERLAY,
	BlendType.DIFFERENCE: bType.DIFFERENCE,
	BlendType.LIGHTEN: bType.LIGHTEN,
	BlendType.DARKEN: bType.DARKEN,
	BlendType.SCREEN: bType.SCREEN,
	BlendType.SOFTLIGHT: bType.SOFTLIGHT,
	BlendType.HARDLIGHT: bType.HARDLIGHT,
	BlendType.GRAINEXTRACT: bType.GRAINEXTRACT,
	BlendType.GRAINMERGE: bType.GRAINMERGE,
	BlendType.DIVIDE: bType.DIVIDE,
	BlendType.HUE: bType.HUE,
	BlendType.SATURATION: bType.SATURATION,
	BlendType.COLOUR: bType.COLOUR,
	BlendType.LUMINOSITY: bType.LUMINOSITY,
	BlendType.XOR: bType.XOR,
	BlendType.NEGATION: bType.NEGATION,
	BlendType.PINLIGHT: bType.PINLIGHT,
	BlendType.VIVIDLIGHT: bType.VIVIDLIGHT,
	BlendType.EXCLUSION: bType.EXCLUSION,
	BlendType.DESTIN: bType.DESTIN,
	BlendType.DESTOUT: bType.DESTOUT,
	BlendType.DESTATOP: bType.DESTATOP,
	BlendType.SRCATOP: bType.SRCATOP}
	return bLayers(background, foreground, blendTypeMap[blendType], opacity)
