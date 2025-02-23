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
	from gimpformats.gimpXcfDocument import GimpDocument, GimpGroup

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

	root_group = project.walkTree()

	def rec_walk(group: GimpGroup) -> list[Group | Layer]:
		layers = []
		for child in group.children[::-1]:
			if isinstance(child, GimpGroup):
				info = child.layer_options
				if info is not None:
					layers.append(
						Group(
							name=str(info.name),
							layers=rec_walk(child),
							dimensions=(info.width, info.height),
							offsets=(0, 0),
							opacity=info.opacity,
							visible=info.visible,
							blendmode=blendModeLookup(info.blendMode, blendLookup),
						)
					)
			else:
				layers.append(
					Layer(
						name=str(child.name),
						image=child.image,
						dimensions=(child.width, child.height),
						offsets=(
							child.xOffset,
							child.yOffset,
						),
						opacity=child.opacity,
						visible=child.visible,
						blendmode=blendModeLookup(child.blendMode, blendLookup),
					)
				)
		return layers

	layersAndGroups = rec_walk(root_group)

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
