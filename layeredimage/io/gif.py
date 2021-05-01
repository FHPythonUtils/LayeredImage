"""Do file io - GIF."""
from __future__ import annotations

from PIL import Image

from ..layeredimage import LayeredImage
from ..layergroup import Layer
from .common import expandLayersToCanvas

# pylint: disable=invalid-name


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
				"Frame {} ({}ms)".format(len(layers) + 1, project.info["duration"]),
				project.copy(),
				projectSize,
			)
		)
	project.close()
	return LayeredImage(layers, projectSize)


def saveLayer_GIF(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .gif."""
	layers = expandLayersToCanvas(layeredImage, "GIF")
	layers[0].save(fileName, duration=100, save_all=True, append_images=layers[1:])
