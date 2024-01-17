"""Example program to convert layered images to ora."""

from __future__ import annotations

import contextlib
from os import listdir
from os.path import isfile, join
from pathlib import Path

import layeredimage.io

THISDIR = str(Path(__file__).resolve().parent)

files = [join(THISDIR, file) for file in listdir(THISDIR) if isfile(join(THISDIR, file))]
for file in files:
	with contextlib.suppress(ValueError):
		layeredimage.io.saveLayerImage(file + ".ora", layeredimage.io.openLayerImage(file))
