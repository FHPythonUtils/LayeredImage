"""Do file io - PDN."""
from __future__ import annotations

from PIL import Image

from ..blend import BlendType
from ..layeredimage import LayeredImage
from ..layergroup import Layer
from .common import blendModeLookup

# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


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
				layer.name,
				image,
				image.size,
				(0, 0),
				layer.opacity / 255,
				layer.visible,
				blendModeLookup(layer.blendMode, blendLookup),
			)
		)
	return LayeredImage(layers, (project.width, project.height))


def saveLayer_PDN(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .pdn."""
	del fileName, layeredImage
	print("ERROR: Saving PDNs is not implemented in pypdn")
	raise NotImplementedError
