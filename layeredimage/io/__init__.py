"""Do file io."""
from __future__ import annotations

from os.path import exists, splitext
from pathlib import Path

from ..layeredimage import LayeredImage
from .gif import openLayer_GIF, saveLayer_GIF
from .layered import (
	openLayer_LAYERED,
	openLayer_LAYEREDC,
	saveLayer_LAYERED,
	saveLayer_LAYEREDC,
)
from .lsr import openLayer_LSR, saveLayer_LSR
from .ora import openLayer_ORA, saveLayer_ORA
from .pdn import openLayer_PDN, saveLayer_PDN
from .psd import openLayer_PSD, saveLayer_PSD
from .tiff import openLayer_TIFF, saveLayer_TIFF
from .webp import openLayer_WEBP, saveLayer_WEBP
from .xcf import openLayer_XCF, saveLayer_XCF


def extNotRecognised(fileName: str):
	"""Output the file extension not recognised error."""
	exts = ["ora", "psd", "xcf", "pdn", "tif", "tiff", "webp", "gif", "lsr", "layered", "layeredc"]
	print(
		f"ERROR: File extension is not recognised for file: {fileName}! Must be one of "
		', "'.join(exts) + '"'
	)


def openLayerImage(file: str | Path) -> LayeredImage:
	"""Open a layer image file into a layer image object.

	Args:
		file (str): path/ filename

	Raises:
		FileExistsError: If the layered image does not exist
		ValueError: If the extention is not recognised

	Returns:
		LayeredImage: a layered image object
	"""
	functionMap = {
		"ora": openLayer_ORA,
		"psd": openLayer_PSD,
		"xcf": openLayer_XCF,
		"pdn": openLayer_PDN,
		"tif": openLayer_TIFF,
		"tiff": openLayer_TIFF,
		"webp": openLayer_WEBP,
		"gif": openLayer_GIF,
		"lsr": openLayer_LSR,
		"layered": openLayer_LAYERED,
		"layeredc": openLayer_LAYEREDC,
	}
	if not exists(file):
		print(f"ERROR: {file} does not exist")
		raise FileExistsError
	fileExt = splitext(file)[1].lower()
	if fileExt not in functionMap:
		extNotRecognised(file)
		raise ValueError
	return functionMap[fileExt](file)


def saveLayerImage(fileName: str | Path, layeredImage: LayeredImage) -> None:
	"""Save a layered image to a file.

	Args:
		fileName (str): path/ filename
		layeredImage (LayeredImage): the layered image to save

	Raises:
		ValueError: If the extention is not recognised

	Returns:
		None
	"""
	functionMap = {
		"ora": saveLayer_ORA,
		"psd": saveLayer_PSD,
		"xcf": saveLayer_XCF,
		"pdn": saveLayer_PDN,
		"tif": saveLayer_TIFF,
		"tiff": saveLayer_TIFF,
		"webp": saveLayer_WEBP,
		"gif": saveLayer_GIF,
		"lsr": saveLayer_LSR,
		"layered": saveLayer_LAYERED,
		"layeredc": saveLayer_LAYEREDC,
	}
	fileExt = splitext(file)[1].lower()
	if fileExt not in functionMap:
		extNotRecognised(fileName)
		raise ValueError
	return functionMap[fileExt](fileName, layeredImage)


def exportFlatImage(fileName: str, layeredImage: LayeredImage) -> None:
	"""Export the layered image to a unilayer image file."""
	layeredImage.getFlattenLayers().save(fileName)
