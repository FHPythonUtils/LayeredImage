"""Do file io - PDN."""

from __future__ import annotations

from blendmodes.blend import BlendType
from loguru import logger
from PIL import Image

from layeredimage.io.common import blendModeLookup
from layeredimage.layeredimage import LayeredImage
from layeredimage.layergroup import Layer


#### PDN ####
def openLayer_PDN(file: str) -> LayeredImage:
	"""Open a .pdn file into a layered image."""
	from pypdn.reader import BlendType as PDNBlend
	from pypdn.reader import read

	blendLookup = {
		PDNBlend.Normal: BlendType.NORMAL,
		PDNBlend.Multiply: BlendType.MULTIPLY,
		PDNBlend.Additive: BlendType.ADDITIVE,
		PDNBlend.ColorBurn: BlendType.COLOURBURN,
		PDNBlend.ColorDodge: BlendType.COLOURDODGE,
		PDNBlend.Reflect: BlendType.REFLECT,
		PDNBlend.Glow: BlendType.GLOW,
		PDNBlend.Overlay: BlendType.OVERLAY,
		PDNBlend.Difference: BlendType.DIFFERENCE,
		PDNBlend.Negation: BlendType.NEGATION,
		PDNBlend.Lighten: BlendType.LIGHTEN,
		PDNBlend.Darken: BlendType.DARKEN,
		PDNBlend.Screen: BlendType.SCREEN,
		PDNBlend.XOR: BlendType.XOR,
	}
	project = read(file)
	layers = []
	for layer in project.layers:
		image = Image.fromarray(layer.image)
		layers.append(
			Layer(
				name=layer.name,
				image=image,
				dimensions=image.size,
				offsets=(0, 0),
				opacity=layer.opacity / 255,
				visible=layer.visible,
				blendmode=blendModeLookup(layer.blendMode, blendLookup),
			)
		)
	return LayeredImage(layers, (project.width, project.height))


def saveLayer_PDN(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .pdn."""
	del fileName, layeredImage
	logger.error("Saving PDNs is not implemented in pypdn")
	raise NotImplementedError
