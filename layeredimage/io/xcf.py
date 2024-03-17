"""Do file io - XCF."""

from __future__ import annotations

from blendmodes.blend import BlendType
from loguru import logger

from layeredimage.io.common import blendModeLookup
from layeredimage.layeredimage import LayeredImage
from layeredimage.layergroup import Group, Layer


#### XCF ####
def openLayer_XCF(file: str) -> LayeredImage:
	"""Open an .xcf file into a layered image."""
	from gimpformats.gimpXcfDocument import GimpDocument

	blendLookup = {
		0: BlendType.NORMAL,
		3: BlendType.MULTIPLY,
		4: BlendType.SCREEN,
		5: BlendType.OVERLAY,
		6: BlendType.DIFFERENCE,
		7: BlendType.ADDITIVE,
		8: BlendType.NEGATION,
		9: BlendType.DARKEN,
		10: BlendType.LIGHTEN,
		11: BlendType.HUE,
		12: BlendType.SATURATION,
		13: BlendType.COLOUR,
		14: BlendType.LUMINOSITY,
		15: BlendType.DIVIDE,
		16: BlendType.COLOURDODGE,
		17: BlendType.COLOURBURN,
		18: BlendType.HARDLIGHT,
		19: BlendType.SOFTLIGHT,
		20: BlendType.GRAINEXTRACT,
		21: BlendType.GRAINMERGE,
		23: BlendType.OVERLAY,
		24: BlendType.HUE,
		25: BlendType.SATURATION,
		26: BlendType.COLOUR,
		27: BlendType.LUMINOSITY,
		28: BlendType.NORMAL,
		30: BlendType.MULTIPLY,
		31: BlendType.SCREEN,
		32: BlendType.DIFFERENCE,
		33: BlendType.ADDITIVE,
		34: BlendType.NEGATION,
		35: BlendType.DARKEN,
		36: BlendType.LIGHTEN,
		37: BlendType.HUE,
		38: BlendType.SATURATION,
		39: BlendType.COLOUR,
		40: BlendType.LUMINOSITY,
		41: BlendType.DIVIDE,
		42: BlendType.COLOURDODGE,
		43: BlendType.COLOURBURN,
		44: BlendType.HARDLIGHT,
		45: BlendType.SOFTLIGHT,
		46: BlendType.GRAINEXTRACT,
		47: BlendType.GRAINMERGE,
		48: BlendType.VIVIDLIGHT,
		49: BlendType.PINLIGHT,
		52: BlendType.EXCLUSION,
	}
	project = GimpDocument(file)
	# Iterate the layers and create a list of layers for each group, then remove
	# these from the project layers
	layers = project.layers[::-1]
	index = 0
	groupIndex = 0
	groupLayers = [[]]
	while index < len(layers):
		layerOrGroup = layers[index]
		if layerOrGroup.isGroup:
			index -= 1
			while layers[index].itemPath is not None:
				layer = layers[index]
				groupLayers[groupIndex].append(
					Layer(
						name=layer.name,
						image=layer.image,
						dimensions=(layer.width, layer.height),
						offsets=(
							layer.xOffset - layerOrGroup.xOffset,
							layer.yOffset - layerOrGroup.yOffset,
						),
						opacity=layer.opacity,
						visible=layer.visible,
						blendmode=blendModeLookup(layer.blendMode, blendLookup),
					)
				)
				layers.pop(index)
				index -= 1
			index += 2
			groupIndex += 1
			groupLayers.append([])
		else:
			index += 1
	# Iterate the clean project layers and add the group layers in
	groupIndex = 0
	layersAndGroups = []
	for layerOrGroup in layers:
		if layerOrGroup.isGroup:
			layersAndGroups.append(
				Group(
					name=layerOrGroup.name,
					layers=groupLayers[groupIndex][::-1],
					dimensions=(layerOrGroup.width, layerOrGroup.height),
					offsets=(layerOrGroup.xOffset, layerOrGroup.yOffset),
					opacity=layerOrGroup.opacity,
					visible=layerOrGroup.visible,
					blendmode=blendModeLookup(layerOrGroup.blendMode, blendLookup),
				)
			)
			groupIndex += 1
		else:
			layersAndGroups.append(
				Layer(
					name=layerOrGroup.name,
					image=layerOrGroup.image,
					dimensions=(layerOrGroup.width, layerOrGroup.height),
					offsets=(layerOrGroup.xOffset, layerOrGroup.yOffset),
					opacity=layerOrGroup.opacity,
					visible=layerOrGroup.visible,
					blendmode=blendModeLookup(layerOrGroup.blendMode, blendLookup),
				)
			)

	return LayeredImage(layersAndGroups, (project.width, project.height))


def saveLayer_XCF(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .xcf."""
	del fileName, layeredImage
	logger.error(
		"Saving XCFs is not implemented in gimpformats - "
		"this is a little misleading as functions are present, however these are not "
		"functional"
	)
	raise NotImplementedError
