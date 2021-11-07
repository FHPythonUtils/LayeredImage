"""Do file io - LSR."""
from __future__ import annotations

from os import sep

from blendmodes.imagetools import renderWAlphaOffset

from ..layeredimage import LayeredImage
from ..layergroup import Group, Layer

# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


## LSR ##
def openLayer_LSR(file: str) -> LayeredImage:
	"""Open a .lsr file into a layered image."""
	import pylsr

	project = pylsr.read(file)
	groups = []
	for group in project.layers:
		groups.append(
			Group(
				group.name,
				[
					Layer(layer.name, layer.scaledImage(), layer.scaledImage().size)
					for layer in group.images
				],
				group.size,
				(int(group.offsets()[0]), int(group.offsets()[1])),
			)
		)
	return LayeredImage(groups, project.size)


def saveLayer_LSR(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .lsr."""
	import pylsr

	layers = []
	for group in layeredImage.layersAndGroups:
		if isinstance(group, Layer):
			imageData = [pylsr.LSRImageData(group.image, group.name)]
		else:
			imageData = [
				pylsr.LSRImageData(
					renderWAlphaOffset(layer.image, group.dimensions, layer.opacity, layer.offsets),
					layer.name,
				)
				for layer in group.layers
			]
		layers.append(
			pylsr.LSRLayer(
				imageData,
				group.name,
				group.dimensions,
				(
					group.offsets[0] + group.dimensions[0] // 2,
					group.offsets[1] + group.dimensions[1] // 2,
				),
			)
		)
	lsrImage = pylsr.LSRImage(
		layeredImage.dimensions, fileName.split(sep)[-1].replace(".lsr", ""), layers
	)
	pylsr.write(fileName, lsrImage)
