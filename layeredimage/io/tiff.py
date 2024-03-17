"""Do file io - TIFF."""

from __future__ import annotations

from PIL import Image

from layeredimage.io.common import expandLayersToCanvas
from layeredimage.layeredimage import LayeredImage
from layeredimage.layergroup import Layer


#### TIFF ####
def openLayer_TIFF(file: str) -> LayeredImage:
	"""Open a .tiff or a .tif file into a layered image."""
	project = Image.open(file)
	layers = []
	dimensions = [0, 0]
	for index in range(project.n_frames):
		# Load the correct image
		project.seek(index)
		# Update the project dimensions
		for indx, dimension in enumerate(dimensions):
			if project.size[indx] > dimension:
				dimensions[indx] = project.size[indx]
		ifd = project.ifd.named()
		# Offsets
		offsetX = 0
		offsetY = 0
		if "XPosition" in ifd:
			offsetX = int(
				ifd["XPosition"][0][0] / ifd["XPosition"][0][1] * ifd["XResolution"][0][0]
			)
		if "YPosition" in ifd:
			offsetY = int(
				ifd["YPosition"][0][0] / ifd["YPosition"][0][1] * ifd["YResolution"][0][0]
			)
		# Add the layer
		layers.append(
			Layer(
				name=ifd["PageName"][0],
				image=project.copy(),
				dimensions=(ifd["ImageWidth"][0], ifd["ImageLength"][0]),
				offsets=(offsetX, offsetY),
				opacity=1,
				visible=True,
			)
		)
	project.close()
	return LayeredImage(layers, (dimensions[0], dimensions[1]))


def saveLayer_TIFF(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .tiff or .tif."""
	layers = expandLayersToCanvas(layeredImage, "TIFF")
	layers[0].save(fileName, compression=None, save_all=True, append_images=layers[1:])
