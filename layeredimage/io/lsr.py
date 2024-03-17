"""Do file io - LSR."""

from __future__ import annotations

from pathlib import Path

from layeredimage.io.common import expandLayer
from layeredimage.layeredimage import LayeredImage
from layeredimage.layergroup import Group, Layer


## LSR ##
def openLayer_LSR(file: str) -> LayeredImage:
	"""Open a .lsr file into a layered image."""
	import pylsr

	project = pylsr.read(file)
	groups = []
	for group in project.layers:
		groups.append(
			Group(
				name=group.name,
				layers=[
					Layer(
						name=layer.name,
						image=layer.scaledImage(),
						dimensions=layer.scaledImage().size,
					)
					for layer in group.images
				],
				dimensions=group.size,
				offsets=(int(group.offsets()[0]), int(group.offsets()[1])),
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
					expandLayer(
						dimensions=group.dimensions,
						foreground=layer.image,
						opacity=layer.opacity,
						offsets=layer.offsets,
					),
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
		size=layeredImage.dimensions, name=Path(fileName).name.replace(".lsr", ""), layers=layers
	)
	pylsr.write(fileName, lsrImage)
