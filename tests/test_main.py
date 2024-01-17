"""Test module """

from __future__ import annotations

import os
import sys
from pathlib import Path

from imgcompare import is_equal

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))

import layeredimage.io


# ORA
def test_ora():
	ora = layeredimage.io.openLayerImage(f"{THISDIR}/data/layered_image.ora")
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/ora_output.ora", ora)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/ora_output.tiff", ora)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/ora_output.webp", ora)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/ora_output.gif", ora)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/ora_output.layered", ora)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/ora_output.layeredc", ora)
	ora.getFlattenLayers().save(f"{THISDIR}/data/ora_output.png")
	assert is_equal(
		f"{THISDIR}/data/ora_output.png",
		f"{THISDIR}/data/layered_image_expected.png",
		tolerance=0.2,
	)


# PSD
def test_psd():
	psd = layeredimage.io.openLayerImage(f"{THISDIR}/data/layered_image.psd")
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/psd_output.ora", psd)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/psd_output.tiff", psd)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/psd_output.webp", psd)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/psd_output.gif", psd)
	psd.getFlattenLayers().save(f"{THISDIR}/data/psd_output.png")
	assert is_equal(
		f"{THISDIR}/data/psd_output.png",
		f"{THISDIR}/data/layered_image_expected.png",
		tolerance=0.2,
	)


# PDN
def test_pdn():
	pdn = layeredimage.io.openLayerImage(f"{THISDIR}/data/layered_image.pdn")
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/pdn_output.ora", pdn)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/pdn_output.tiff", pdn)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/pdn_output.webp", pdn)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/pdn_output.gif", pdn)
	pdn.getFlattenLayers().save(f"{THISDIR}/data/pdn_output.png")
	assert is_equal(
		f"{THISDIR}/data/pdn_output.png",
		f"{THISDIR}/data/layered_image_expected.png",
		tolerance=0.2,
	)


# XCF
def test_xcf():
	xcf = layeredimage.io.openLayerImage(f"{THISDIR}/data/layered_image.xcf")
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/xcf_output.ora", xcf)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/xcf_output.tiff", xcf)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/xcf_output.webp", xcf)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/xcf_output.gif", xcf)
	xcf.getFlattenLayers().save(f"{THISDIR}/data/xcf_output.png")
	assert is_equal(
		f"{THISDIR}/data/xcf_output.png",
		f"{THISDIR}/data/layered_image_expected.png",
		tolerance=0.2,
	)


# TIFF
def test_tiff():
	tiff = layeredimage.io.openLayerImage(f"{THISDIR}/data/layered_image.tiff")
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/tiff_output.ora", tiff)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/tiff_output.tiff", tiff)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/tiff_output.webp", tiff)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/tiff_output.gif", tiff)
	tiff.getFlattenLayers().save(f"{THISDIR}/data/tiff_output.png")
	assert is_equal(
		f"{THISDIR}/data/tiff_output.png",
		f"{THISDIR}/data/layered_image_expected_nh.png",
		tolerance=0.2,
	)


# WEBP
def test_webp():
	webp = layeredimage.io.openLayerImage(f"{THISDIR}/data/layered_image.webp")
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/webp_output.ora", webp)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/webp_output.webp", webp)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/webp_output.webp", webp)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/webp_output.gif", webp)
	webp.getFlattenLayers().save(f"{THISDIR}/data/webp_output.png")
	assert is_equal(
		f"{THISDIR}/data/webp_output.png",
		f"{THISDIR}/data/layered_image_expected_nh.png",
		tolerance=0.2,
	)


# GIF
def test_gif():
	gif = layeredimage.io.openLayerImage(f"{THISDIR}/data/layered_image.gif")
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/gif_output.ora", gif)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/gif_output.gif", gif)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/gif_output.webp", gif)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/gif_output.gif", gif)
	gif.getFlattenLayers().save(f"{THISDIR}/data/gif_output.png")
	assert is_equal(
		f"{THISDIR}/data/gif_output.png", f"{THISDIR}/data/gif_output_expected.png", tolerance=0.2
	)


# LSR
def test_lsr():
	lsr = layeredimage.io.openLayerImage(f"{THISDIR}/data/layered_image.lsr")
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/lsr_output.ora", lsr)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/lsr_output.lsr", lsr)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/lsr_output.webp", lsr)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/lsr_output.lsr", lsr)
	lsr.getFlattenLayers().save(f"{THISDIR}/data/lsr_output.png")
	assert is_equal(
		f"{THISDIR}/data/lsr_output.png",
		f"{THISDIR}/data/layered_image_expected_nh.png",
		tolerance=0.2,
	)


# LAYERED
def test_layered():
	layered = layeredimage.io.openLayerImage(f"{THISDIR}/data/layered_image.layered")
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/layered_output.ora", layered)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/layered_output.tiff", layered)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/layered_output.webp", layered)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/layered_output.gif", layered)
	layered.getFlattenLayers().save(f"{THISDIR}/data/layered_output.png")
	assert is_equal(
		f"{THISDIR}/data/layered_output.png",
		f"{THISDIR}/data/layered_image_expected.png",
		tolerance=0.2,
	)


# LAYEREDC
def test_layeredc():
	layeredc = layeredimage.io.openLayerImage(f"{THISDIR}/data/layered_image.layeredc")
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/layeredc_output.ora", layeredc)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/layeredc_output.tiff", layeredc)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/layeredc_output.webp", layeredc)
	layeredimage.io.saveLayerImage(f"{THISDIR}/data/layeredc_output.gif", layeredc)
	layeredc.getFlattenLayers().save(f"{THISDIR}/data/layeredc_output.png")
	assert is_equal(
		f"{THISDIR}/data/layeredc_output.png",
		f"{THISDIR}/data/layered_image_expected.png",
		tolerance=0.2,
	)


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
