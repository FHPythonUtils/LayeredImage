"""Test module """

import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from imgcompare import is_equal
import layeredimage.io

#pylint: disable=missing-function-docstring

# ORA
def test_ora():
	ora = layeredimage.io.openLayerImage(THISDIR + "/base24.ora")
	layeredimage.io.saveLayerImage(THISDIR + "/base24(ora).ora", ora)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(ora).tiff", ora)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(ora).webp", ora)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(ora).gif", ora)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(ora).layered", ora)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(ora).layeredc", ora)
	ora.getFlattenLayers().save(THISDIR + "/base24(ora).png")
	assert(is_equal(THISDIR + "/base24(ora).png", THISDIR + "/expected.png", tolerance=1))

# PSD
def test_psd():
	psd = layeredimage.io.openLayerImage(THISDIR + "/base24.psd")
	layeredimage.io.saveLayerImage(THISDIR + "/base24(psd).ora", psd)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(psd).tiff", psd)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(psd).webp", psd)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(psd).gif", psd)
	psd.getFlattenLayers().save(THISDIR + "/base24(psd).png")
	assert(is_equal(THISDIR + "/base24(psd).png", THISDIR + "/expected.png", tolerance=1))

# PDN
def test_pdn():
	pdn = layeredimage.io.openLayerImage(THISDIR + "/base24.pdn")
	layeredimage.io.saveLayerImage(THISDIR + "/base24(pdn).ora", pdn)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(pdn).tiff", pdn)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(pdn).webp", pdn)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(pdn).gif", pdn)
	pdn.getFlattenLayers().save(THISDIR + "/base24(pdn).png")
	assert(is_equal(THISDIR + "/base24(pdn).png", THISDIR + "/expected.png", tolerance=1))

# XCF
def test_xcf():
	xcf = layeredimage.io.openLayerImage(THISDIR + "/base24.xcf")
	layeredimage.io.saveLayerImage(THISDIR + "/base24(xcf).ora", xcf)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(xcf).tiff", xcf)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(xcf).webp", xcf)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(xcf).gif", xcf)
	xcf.getFlattenLayers().save(THISDIR + "/base24(xcf).png")
	assert(is_equal(THISDIR + "/base24(xcf).png", THISDIR + "/expected.png", tolerance=1))

# TIFF
def test_tiff():
	tiff = layeredimage.io.openLayerImage(THISDIR + "/base24.tiff")
	layeredimage.io.saveLayerImage(THISDIR + "/base24(tiff).ora", tiff)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(tiff).tiff", tiff)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(tiff).webp", tiff)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(tiff).gif", tiff)
	tiff.getFlattenLayers().save(THISDIR + "/base24(tiff).png")
	assert(is_equal(THISDIR + "/base24(tiff).png", THISDIR + "/expectedNoHidden.png", tolerance=1))

# WEBP
def test_webp():
	webp = layeredimage.io.openLayerImage(THISDIR + "/base24.webp")
	layeredimage.io.saveLayerImage(THISDIR + "/base24(webp).ora", webp)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(webp).webp", webp)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(webp).webp", webp)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(webp).gif", webp)
	webp.getFlattenLayers().save(THISDIR + "/base24(webp).png")
	assert(is_equal(THISDIR + "/base24(webp).png", THISDIR + "/expectedNoHidden.png", tolerance=1))

# GIF
def test_gif():
	gif = layeredimage.io.openLayerImage(THISDIR + "/base24.gif")
	layeredimage.io.saveLayerImage(THISDIR + "/base24(gif).ora", gif)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(gif).gif", gif)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(gif).webp", gif)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(gif).gif", gif)
	gif.getFlattenLayers().save(THISDIR + "/base24(gif).png")
	assert(is_equal(THISDIR + "/base24(gif).png", THISDIR + "/expectedNoHidden.png", tolerance=1))

# LSR
def test_lsr():
	lsr = layeredimage.io.openLayerImage(THISDIR + "/base24.lsr")
	layeredimage.io.saveLayerImage(THISDIR + "/base24(lsr).ora", lsr)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(lsr).lsr", lsr)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(lsr).webp", lsr)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(lsr).lsr", lsr)
	lsr.getFlattenLayers().save(THISDIR + "/base24(lsr).png")
	assert(is_equal(THISDIR + "/base24(lsr).png", THISDIR + "/expectedNoHidden.png", tolerance=1))

# LAYERED
def test_layered():
	layered = layeredimage.io.openLayerImage(THISDIR + "/base24.layered")
	layeredimage.io.saveLayerImage(THISDIR + "/base24(layered).ora", layered)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(layered).tiff", layered)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(layered).webp", layered)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(layered).gif", layered)
	layered.getFlattenLayers().save(THISDIR + "/base24(layered).png")
	assert(is_equal(THISDIR + "/base24(layered).png", THISDIR + "/expected.png", tolerance=1))

# LAYEREDC
def test_layeredc():
	layeredc = layeredimage.io.openLayerImage(THISDIR + "/base24.layeredc")
	layeredimage.io.saveLayerImage(THISDIR + "/base24(layeredc).ora", layeredc)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(layeredc).tiff", layeredc)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(layeredc).webp", layeredc)
	layeredimage.io.saveLayerImage(THISDIR + "/base24(layeredc).gif", layeredc)
	layeredc.getFlattenLayers().save(THISDIR + "/base24(layeredc).png")
	assert(is_equal(THISDIR + "/base24(layeredc).png", THISDIR + "/expected.png", tolerance=1))


if __name__ == "__main__":
	test_ora()
	test_psd()
	test_pdn()
	test_xcf()
	test_tiff()
	test_webp()
	test_gif()
	test_lsr()
	test_layered()
	test_layeredc()
