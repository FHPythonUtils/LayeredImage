"""Do file io - PSD."""
from __future__ import annotations

from ..blend import BlendType
from ..layeredimage import LayeredImage
from ..layergroup import Group, Layer
from .common import blendModeLookup


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
						layer.name,
						layer.topil(),
						(layer.width, layer.height),
						(layer.left - layerOrGroup.left, layer.top - layerOrGroup.top),
						layer.opacity / 255,
						layer.visible,
						blendModeLookup(layer.blend_mode, blendLookup),
					)
				)
			layersAndGroups.append(
				Group(
					layerOrGroup.name,
					layers,
					(layerOrGroup.width, layerOrGroup.height),
					(layerOrGroup.left, layerOrGroup.top),
					layerOrGroup.opacity / 255,
					layerOrGroup.visible,
					blendModeLookup(layerOrGroup.blend_mode, blendLookup),
				)
			)
		else:
			layersAndGroups.append(
				Layer(
					layerOrGroup.name,
					layerOrGroup.topil(),
					(layerOrGroup.width, layerOrGroup.height),
					(layerOrGroup.left, layerOrGroup.top),
					layerOrGroup.opacity / 255,
					layerOrGroup.visible,
					blendModeLookup(layerOrGroup.blend_mode, blendLookup),
				)
			)
	return LayeredImage(layersAndGroups, (project.width, project.height))


def saveLayer_PSD(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .psd."""
	del fileName, layeredImage
	print("ERROR: Saving PSDs is not implemented in psd-tools3")
	raise NotImplementedError
