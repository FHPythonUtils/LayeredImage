"""Test module """

import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
import layeredimage.io

# Read various formats and output ora
ora = layeredimage.io.openLayerImage(THISDIR + "/base24.ora")
psd = layeredimage.io.openLayerImage(THISDIR + "/base24.psd")
pdn = layeredimage.io.openLayerImage(THISDIR + "/base24.pdn")
xcf = layeredimage.io.openLayerImage(THISDIR + "/base24.xcf")

layeredimage.io.saveLayerImage(THISDIR + "/base24(ora).ora", ora)
layeredimage.io.saveLayerImage(THISDIR + "/base24(psd).ora", psd)
layeredimage.io.saveLayerImage(THISDIR + "/base24(pdn).ora", pdn)
layeredimage.io.saveLayerImage(THISDIR + "/base24(xcf).ora", xcf)

# Output flattened images
ora.getFlattenLayers().save(THISDIR + "/base24(ora).png")
psd.getFlattenLayers().save(THISDIR + "/base24(psd).png")
pdn.getFlattenLayers().save(THISDIR + "/base24(pdn).png")
xcf.getFlattenLayers().save(THISDIR + "/base24(xcf).png")
