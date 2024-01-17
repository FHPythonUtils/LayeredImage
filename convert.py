"""Example program to convert layered images to ora."""

from __future__ import annotations

import contextlib
from os import listdir
from pathlib import Path

import layeredimage.io

THISDIR = Path(__file__).resolve().parent

files = [THISDIR / file for file in listdir(THISDIR) if (THISDIR / file).is_file()]
for file in files:
	with contextlib.suppress(ValueError):
		layeredimage.io.saveLayerImage(f"{file}.ora", layeredimage.io.openLayerImage(file))
