"""Do file io - GIF."""

from __future__ import annotations

from PIL import Image

from layeredimage.io.common import expandLayersToCanvas
from layeredimage.layeredimage import LayeredImage
from layeredimage.layergroup import Layer


## GIF ##
def openLayer_GIF(file: str) -> LayeredImage:
	"""Open a .gif file into a layered image."""
	project = Image.open(file)
	projectSize = project.size
	layers = []
	for index in range(project.n_frames):
		project.seek(index)
		layers.append(
			Layer(
				name=f"Frame {len(layers) + 1} ({project.info['duration']}ms)",
				image=project.copy(),
				dimensions=projectSize,
			)
		)
	project.close()
	return LayeredImage(layers, projectSize)


def saveLayer_GIF(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .gif."""
	layers = expandLayersToCanvas(layeredImage, "GIF")
	layers[0].save(
		fileName,
		duration=200,
		append_images=layers[1:],
		version="GIF89a",
		disposal=2,
		save_all=True,
		loop=0,
		transparency=0,
	)
