"""Do file io - PSD."""

from __future__ import annotations

from blendmodes.blend import BlendType
from loguru import logger

from layeredimage.io.common import blendModeLookup
from layeredimage.layeredimage import LayeredImage
from layeredimage.layergroup import Group, Layer


#### PSD ####
def openLayer_PSD(file: str) -> LayeredImage:
	"""Open a .psd file into a layered image."""
	from psd_tools import PSDImage
	from psd_tools.constants import BlendMode as psdB

	blendLookup = {
		psdB.NORMAL: BlendType.NORMAL,
		psdB.MULTIPLY: BlendType.MULTIPLY,
		psdB.COLOR_BURN: BlendType.COLOURBURN,
		psdB.COLOR_DODGE: BlendType.COLOURDODGE,
		psdB.OVERLAY: BlendType.OVERLAY,
		psdB.DIFFERENCE: BlendType.DIFFERENCE,
		psdB.SUBTRACT: BlendType.NEGATION,
		psdB.LIGHTEN: BlendType.LIGHTEN,
		psdB.DARKEN: BlendType.DARKEN,
		psdB.SCREEN: BlendType.SCREEN,
		psdB.SOFT_LIGHT: BlendType.SOFTLIGHT,
		psdB.HARD_LIGHT: BlendType.HARDLIGHT,
		psdB.EXCLUSION: BlendType.EXCLUSION,
		psdB.HUE: BlendType.HUE,
		psdB.SATURATION: BlendType.SATURATION,
		psdB.COLOR: BlendType.COLOUR,
		psdB.LUMINOSITY: BlendType.LUMINOSITY,
		psdB.DIVIDE: BlendType.DIVIDE,
		psdB.PIN_LIGHT: BlendType.PINLIGHT,
		psdB.VIVID_LIGHT: BlendType.VIVIDLIGHT,
	}
	layersAndGroups = []
	project = PSDImage.open(file)
	for layerOrGroup in project:
		if layerOrGroup.is_group():
			layers = []
			for layer in layerOrGroup:
				layers.append(
					Layer(
						name=layer.name,
						image=layer.topil(),
						dimensions=(layer.width, layer.height),
						offsets=(layer.left - layerOrGroup.left, layer.top - layerOrGroup.top),
						opacity=layer.opacity / 255,
						visible=layer.visible,
						blendmode=blendModeLookup(layer.blend_mode, blendLookup),
					)
				)
			layersAndGroups.append(
				Group(
					name=layerOrGroup.name,
					layers=layers,
					dimensions=(layerOrGroup.width, layerOrGroup.height),
					offsets=(layerOrGroup.left, layerOrGroup.top),
					opacity=layerOrGroup.opacity / 255,
					visible=layerOrGroup.visible,
					blendmode=blendModeLookup(layerOrGroup.blend_mode, blendLookup),
				)
			)
		else:
			layersAndGroups.append(
				Layer(
					name=layerOrGroup.name,
					image=layerOrGroup.topil(),
					dimensions=(layerOrGroup.width, layerOrGroup.height),
					offsets=(layerOrGroup.left, layerOrGroup.top),
					opacity=layerOrGroup.opacity / 255,
					visible=layerOrGroup.visible,
					blendmode=blendModeLookup(layerOrGroup.blend_mode, blendLookup),
				)
			)
	return LayeredImage(layersAndGroups, (project.width, project.height))


def saveLayer_PSD(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .psd."""
	del fileName, layeredImage
	logger.error("Saving PSDs is not implemented in psd-tools3")
	raise NotImplementedError
