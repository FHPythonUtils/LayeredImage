"""Test module """

import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
import layeredimage.io

# ORA
ora = layeredimage.io.openLayerImage(THISDIR + "/base24.ora")
layeredimage.io.saveLayerImage(THISDIR + "/base24(ora).ora", ora)
layeredimage.io.saveLayerImage(THISDIR + "/base24(ora).tiff", ora)
ora.getFlattenLayers().save(THISDIR + "/base24(ora).png")

# PSD
psd = layeredimage.io.openLayerImage(THISDIR + "/base24.psd")
layeredimage.io.saveLayerImage(THISDIR + "/base24(psd).ora", psd)
layeredimage.io.saveLayerImage(THISDIR + "/base24(psd).tiff", psd)
psd.getFlattenLayers().save(THISDIR + "/base24(psd).png")

# PDN
if sys.version_info[0] >= 3 and sys.version_info[1] < 8:
	pdn = layeredimage.io.openLayerImage(THISDIR + "/base24.pdn")
	layeredimage.io.saveLayerImage(THISDIR + "/base24(pdn).ora", pdn)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(pdn).tiff", pdn)
	pdn.getFlattenLayers().save(THISDIR + "/base24(pdn).png")

# XCF
xcf = layeredimage.io.openLayerImage(THISDIR + "/base24.xcf")
layeredimage.io.saveLayerImage(THISDIR + "/base24(xcf).ora", xcf)
layeredimage.io.saveLayerImage(THISDIR + "/base24(xcf).tiff", xcf)
xcf.getFlattenLayers().save(THISDIR + "/base24(xcf).png")

# TIFF
tiff = layeredimage.io.openLayerImage(THISDIR + "/base24.tiff")
layeredimage.io.saveLayerImage(THISDIR + "/base24(tiff).ora", tiff)
layeredimage.io.saveLayerImage(THISDIR + "/base24(tiff).tiff", tiff)
tiff.getFlattenLayers().save(THISDIR + "/base24(tiff).png")
