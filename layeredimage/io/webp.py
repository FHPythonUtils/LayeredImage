"""Do file io - WEBP."""

from __future__ import annotations

from PIL import Image

from layeredimage.io.common import expandLayersToCanvas
from layeredimage.layeredimage import LayeredImage
from layeredimage.layergroup import Layer


## WEBP ##
def openLayer_WEBP(file: str) -> LayeredImage:
	"""Open a .webp file into a layered image."""
	project = Image.open(file)
	projectSize = project.size
	layers = []
	for index in range(project.n_frames):
		project.seek(index)
		layers.append(
			Layer(name=f"Frame {len(layers) + 1}", image=project.copy(), dimensions=projectSize)
		)
	project.close()
	return LayeredImage(layers, projectSize)


def saveLayer_WEBP(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .webp."""
	layers = expandLayersToCanvas(layeredImage, "WEBP")
	layers[0].save(fileName, duration=200, save_all=True, append_images=layers[1:])
