""" example program to convert layered images to ora """

from os.path import isfile, join
from os import listdir
from pathlib import Path
import layeredimage.io

THISDIR = str(Path(__file__).resolve().parent)

files = [
join(THISDIR, file) for file in listdir(THISDIR)
if isfile(join(THISDIR, file))]
for file in files:
	try:
		layeredimage.io.saveLayerImage(file + ".ora", layeredimage.io.openLayerImage(file))
	except ValueError:
		pass
