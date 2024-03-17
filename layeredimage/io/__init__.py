"""Do file io."""

from __future__ import annotations

from pathlib import Path

from loguru import logger

from layeredimage.io.gif import openLayer_GIF, saveLayer_GIF
from layeredimage.io.layered import (
	openLayer_LAYERED,
	openLayer_LAYEREDC,
	saveLayer_LAYERED,
	saveLayer_LAYEREDC,
)
from layeredimage.io.lsr import openLayer_LSR, saveLayer_LSR
from layeredimage.io.ora import openLayer_ORA, saveLayer_ORA
from layeredimage.io.pdn import openLayer_PDN, saveLayer_PDN
from layeredimage.io.psd import openLayer_PSD, saveLayer_PSD
from layeredimage.io.tiff import openLayer_TIFF, saveLayer_TIFF
from layeredimage.io.webp import openLayer_WEBP, saveLayer_WEBP
from layeredimage.io.xcf import openLayer_XCF, saveLayer_XCF
from layeredimage.layeredimage import LayeredImage


def extNotRecognised(fileName: str) -> None:
	"""Output the file extension not recognised error."""
	exts = ["ora", "psd", "xcf", "pdn", "tif", "tiff", "webp", "gif", "lsr", "layered", "layeredc"]
	logger.error(
		".File extension is not recognised for file! Must be one of " + ', "'.join(exts) + '"',
		extra={"fileName": fileName},
	)


def openLayerImage(file: str | Path) -> LayeredImage:
	"""Open a layer image file into a layer image object.

	Args:
	----
		file (str): path/ filename

	Raises:
	------
		FileExistsError: If the layered image does not exist
		ValueError: If the extention is not recognised

	Returns:
	-------
		LayeredImage: a layered image object

	"""
	functionMap = {
		".ora": openLayer_ORA,
		".psd": openLayer_PSD,
		".xcf": openLayer_XCF,
		".pdn": openLayer_PDN,
		".tif": openLayer_TIFF,
		".tiff": openLayer_TIFF,
		".webp": openLayer_WEBP,
		".gif": openLayer_GIF,
		".lsr": openLayer_LSR,
		".layered": openLayer_LAYERED,
		".layeredc": openLayer_LAYEREDC,
	}
	fp = Path(file)
	if not fp.is_file():
		logger.error("File does not exist", extra={"file": file})
		raise FileExistsError
	fileExt = fp.suffix.lower()
	if fileExt not in functionMap:
		extNotRecognised(fp.name)
		raise ValueError
	return functionMap[fileExt](fp.as_posix())


def saveLayerImage(fileName: str | Path, layeredImage: LayeredImage) -> None:
	"""Save a layered image to a file.

	Args:
	----
		fileName (str): path/ filename
		layeredImage (LayeredImage): the layered image to save

	Raises:
	------
		ValueError: If the extention is not recognised

	Returns:
	-------
		None

	"""
	functionMap = {
		".ora": saveLayer_ORA,
		".psd": saveLayer_PSD,
		".xcf": saveLayer_XCF,
		".pdn": saveLayer_PDN,
		".tif": saveLayer_TIFF,
		".tiff": saveLayer_TIFF,
		".webp": saveLayer_WEBP,
		".gif": saveLayer_GIF,
		".lsr": saveLayer_LSR,
		".layered": saveLayer_LAYERED,
		".layeredc": saveLayer_LAYEREDC,
	}
	pth = Path(fileName)
	fileExt = pth.suffix.lower()
	if fileExt not in functionMap:
		extNotRecognised(pth.name)
		raise ValueError
	return functionMap[fileExt](pth.as_posix(), layeredImage)


def exportFlatImage(fileName: str, layeredImage: LayeredImage) -> None:
	"""Export the layered image to a unilayer image file."""
	layeredImage.getFlattenLayers().save(fileName)
