[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/LayeredImage.svg?style=for-the-badge&cacheSeconds=28800)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/LayeredImage.svg?style=for-the-badge&cacheSeconds=28800)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/LayeredImage.svg?style=for-the-badge&cacheSeconds=28800)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/LayeredImage.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/LayeredImage.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/layeredimage.svg?style=for-the-badge&cacheSeconds=28800)](https://pypistats.org/packages/layeredimage)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi%2Epepy%2Etech%2Fapi%2Fv2%2Fprojects%2Flayeredimage)](https://pepy.tech/project/layeredimage)
[![PyPI Version](https://img.shields.io/pypi/v/layeredimage.svg?style=for-the-badge&cacheSeconds=28800)](https://pypi.org/project/layeredimage)

<!-- omit in toc -->
# LayeredImage

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Use this module to read, and write to a number of layered image formats

- [Compatibility](#compatibility)
	- [Overview](#overview)
		- [Key](#key)
		- [Reading - Group](#reading---group)
		- [Reading - Layer](#reading---layer)
		- [Writing - Group](#writing---group)
		- [Writing - Layer](#writing---layer)
- [.layered](#layered)
- [Example Usage](#example-usage)
- [Documentation](#documentation)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Windows - Python.org](#windows---pythonorg)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
	- [Dnf](#dnf)
- [Install Python on MacOS](#install-python-on-macos)
	- [Homebrew](#homebrew)
	- [MacOS - Python.org](#macos---pythonorg)
- [How to run](#how-to-run)
	- [Windows](#windows)
	- [Linux/ MacOS](#linux-macos)
- [Building](#building)
- [Testing](#testing)
- [Download Project](#download-project)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)
	- [Rationale](#rationale)

## Compatibility

Bear in mind that the tables below may not be completely accurate. If that is
the case, please open an issue and I will fix the tables.

### Overview

#### Key

- ✔ - Supported
- ⚠ - Things will look the same, but data is lost
- ❌ - This is not supported and will cause loss of data
- N/A - The source format does not support this so treat this as a ✔

| Format | .ora               | .pdn               | .xcf               | .psd               | .tiff/ .tif        | .webp              | .gif               | .lsr               |
| ------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| Read   | ✔                 | ✔                 | ✔                 | ✔                 | ✔                 | ✔                 | ✔                 | ✔                 |
| Layers | ✔                 | ✔                 | ✔                 | ✔                 | ✔                 | ✔                 | ✔                 | ✔                 |
| Groups | ✔                 | N/A                | ✔                 | ✔                 | N/A                | N/A                | N/A                | ✔                 |
| Write  | ✔                 | ❌                | ❌                | ❌                | ⚠                 | ⚠                 | ⚠                 | ✔                 |

#### Reading - Group

| Format     | .ora               | .pdn | .xcf               | .psd               | .tiff/ .tif | .webp | .gif | .lsr               |
| ---------- | ------------------ | ---- | ------------------ | ------------------ | ----------- | ----- | ---- | ------------------ |
| Name       | ✔                 | N/A  | ✔                 | ✔                 | N/A         | N/A   | N/A  | ✔                 |
| Dimensions | ⚠                 | N/A  | ✔                 | ✔                 | N/A         | N/A   | N/A  | ✔                 |
| Offsets    | ✔                 | N/A  | ✔                 | ✔                 | N/A         | N/A   | N/A  | ✔                 |
| Opacity    | ✔                 | N/A  | ✔                 | ✔                 | N/A         | N/A   | N/A  | N/A                |
| Visibility | ✔                 | N/A  | ✔                 | ✔                 | N/A         | N/A   | N/A  | N/A                |
| Blend Mode | ✔                 | N/A  | ✔                 | ✔                 | N/A         | N/A   | N/A  | N/A                |

#### Reading - Layer

| Format     | .ora               | .pdn               | .xcf               | .psd               | .tiff/ .tif        | .webp              | .gif               | .lsr               |
| ---------- | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| Name       | ✔                 | ✔                 | ✔                 | ✔                 | ✔                 | ⚠                 | ⚠                 | ✔                 |
| Dimensions | ✔                 | ✔                 | ✔                 | ✔                 | ✔                 | ✔                 | ✔                 | ✔                 |
| Offsets    | ✔                 | N/A                | ✔                 | ✔                 | ✔                 | N/A                | N/A                | N/A                |
| Opacity    | ✔                 | ✔                 | ✔                 | ✔                 | N/A                | N/A                | N/A                | N/A                |
| Visibility | ✔                 | ✔                 | ✔                 | ✔                 | N/A                | N/A                | N/A                | N/A                |
| Blend Mode | ✔                 | ✔                 | ✔                 | ✔                 | N/A                | N/A                | N/A                | N/A                |

#### Writing - Group

| Format     | .ora               | .pdn | .xcf | .psd | .tiff/ .tif | .webp     | .gif      | .lsr               |
| ---------- | ------------------ | ---- | ---- | ---- | ----------- | --------- | --------- | ------------------ |
| Name       | ✔                 | ❌  | ❌  | ❌  | ❌         | ❌       | ❌       | ✔                 |
| Dimensions | ✔                 | ❌  | ❌  | ❌  | ⚠          | ⚠        | ⚠        | ✔                 |
| Offsets    | ✔                 | ❌  | ❌  | ❌  | ⚠          | ⚠        | ⚠        | ✔                 |
| Opacity    | ✔                 | ❌  | ❌  | ❌  | ⚠          | ⚠        | ⚠        | ⚠                 |
| Visibility | ✔                 | ❌  | ❌  | ❌  | ⚠          | ⚠        | ⚠        | ⚠                 |
| Blend Mode | ✔                 | ❌  | ❌  | ❌  | ❌         | ❌       | ❌       | ❌                |

```none
Layers are extracted from groups and saved to TIFF/ GIF or WEBP
```

#### Writing - Layer

| Format     | .ora               | .pdn | .xcf | .psd | .tiff/ .tif | .webp     | .gif      | .lsr      |
| ---------- | ------------------ | ---- | ---- | ---- | ----------- | --------- | --------- | --------- |
| Name       | ✔                 | ❌  | ❌  | ❌  | ❌         | ❌       | ❌       | ⚠        |
| Dimensions | ✔                 | ❌  | ❌  | ❌  | ⚠          | ⚠        | ⚠        | ⚠        |
| Offsets    | ✔                 | ❌  | ❌  | ❌  | ⚠          | ⚠        | ⚠        | ⚠        |
| Opacity    | ✔                 | ❌  | ❌  | ❌  | ⚠          | ⚠        | ⚠        | ⚠        |
| Visibility | ✔                 | ❌  | ❌  | ❌  | ⚠          | ⚠        | ⚠        | ⚠        |
| Blend Mode | ✔                 | ❌  | ❌  | ❌  | ❌         | ❌       | ❌       | ❌       |

```none
Layers are rendered with offsets before being written to TIFF/ GIF or WEBP
First child layers are placed in a group when written to LSR
```

## .layered

.layered is highly inspired by the open raster format and aims to provide an
exchange format in the cases when saving in ora would cause unacceptable data
loss. .layered has been designed so that if the format became deprecated and no
readers existed for it tomorrow, the data would be easily salvageable.

See the [LAYERED_SPEC](/LAYERED_SPEC.md) for more information.

## Example Usage

Here's some basic example usage below.

```python
"""Example module """
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
import layeredimage.io

# Do stuff
ora = layeredimage.io.openLayerImage(f"{THISDIR}/image.ora")

imageDimensions = ora.dimensions
# There are a load of handy functions for getting layers, and adding new
# layers, but here we will act directly on the object
layer = ora.layersAndGroups[0] # For the sake of the e.g. this is a layer

# Lets overwrite the layer with a transparent image (bit boring I know...)
layer.image = Image.new("RGBA", imageDimensions)
ora.layersAndGroups[0] = layer

# And let's save
layeredimage.io.saveLayerImage(f"{THISDIR}/image(modified).ora", ora)

# Let's save a flattened version too
ora.getFlattenLayers().save(f"{THISDIR}/image(modified).png")

# Doing stuff with a group
group = ora.getLayerOrGroup(1) # For the sake of the e.g. this is a group
group.layers[0].image.show() # Open the image of the first layer of the group

# Deleting a layer/ group
ora.removeLayerOrGroup(2)
```

Images are PIL.Image (s) and so you can use the power of Pillow to apply
filters, and other modifications to the images.

See below for an old version of the tests. These provide a few examples of
file conversions. Not going to get 100% coverage anytime soon but hopefully
this will help a little.

```python
"""Test module """

import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
import layeredimage.io

# ORA
ora = layeredimage.io.openLayerImage(f"{THISDIR}/base24.ora")
layeredimage.io.saveLayerImage(f"{THISDIR}/base24(ora).ora", ora)
layeredimage.io.saveLayerImage(f"{THISDIR}/base24(ora).tiff", ora)
ora.getFlattenLayers().save(f"{THISDIR}/base24(ora).png")

# PSD
psd = layeredimage.io.openLayerImage(f"{THISDIR}/base24.psd")
layeredimage.io.saveLayerImage(f"{THISDIR}/base24(psd).ora", psd)
layeredimage.io.saveLayerImage(f"{THISDIR}/base24(psd).tiff", psd)
psd.getFlattenLayers().save(f"{THISDIR}/base24(psd).png")

# PDN
pdn = layeredimage.io.openLayerImage(f"{THISDIR}/base24.pdn")
layeredimage.io.saveLayerImage(f"{THISDIR}/base24(pdn).ora", pdn)
layeredimage.io.saveLayerImage(f"{THISDIR}/base24(pdn).tiff", pdn)
pdn.getFlattenLayers().save(f"{THISDIR}/base24(pdn).png")

# XCF
xcf = layeredimage.io.openLayerImage(f"{THISDIR}/base24.xcf")
layeredimage.io.saveLayerImage(f"{THISDIR}/base24(xcf).ora", xcf)
layeredimage.io.saveLayerImage(f"{THISDIR}/base24(xcf).tiff", xcf)
xcf.getFlattenLayers().save(f"{THISDIR}/base24(xcf).png")

# TIFF
tiff = layeredimage.io.openLayerImage(f"{THISDIR}/base24.tiff")
layeredimage.io.saveLayerImage(f"{THISDIR}/base24(tiff).ora", tiff)
layeredimage.io.saveLayerImage(f"{THISDIR}/base24(tiff).tiff", tiff)
tiff.getFlattenLayers().save(f"{THISDIR}/base24(tiff).png")
```

## Documentation

A high-level overview of how the documentation is organized organized will help you know
where to look for certain things:

<!--
- [Tutorials](/documentation/tutorials) take you by the hand through a series of steps to get
  started using the software. Start here if you’re new.
-->
- The [Technical Reference](/documentation/reference) documents APIs and other aspects of the
  machinery. This documentation describes how to use the classes and functions at a lower level
  and assume that you have a good high-level understanding of the software.
<!--
- The [Help](/documentation/help) guide provides a starting point and outlines common issues that you
  may have.
-->

## Install With PIP

```python
pip install layeredimage
```

Head to https://pypi.org/project/layeredimage/ for more info

## Language information

### Built for

This program has been written for Python versions 3.8 - 3.11 and has been tested with both 3.8 and
3.11

## Install Python on Windows

### Chocolatey

```powershell
choco install python
```

### Windows - Python.org

To install Python, go to https://www.python.org/downloads/windows/ and download the latest
version.

## Install Python on Linux

### Apt

```bash
sudo apt install python3.x
```

### Dnf

```bash
sudo dnf install python3.x
```

## Install Python on MacOS

### Homebrew

```bash
brew install python@3.x
```

### MacOS - Python.org

To install Python, go to https://www.python.org/downloads/macos/ and download the latest
version.

## How to run

### Windows

- Module
	`py -3.x -m [module]` or `[module]` (if module installs a script)

- File
	`py -3.x [file]` or `./[file]`

### Linux/ MacOS

- Module
	`python3.x -m [module]` or `[module]` (if module installs a script)

- File
	`python3.x [file]` or `./[file]`

## Building

This project uses https://github.com/FHPythonUtils/FHMake to automate most of the building. This
command generates the documentation, updates the requirements.txt and builds the library artefacts

Note the functionality provided by fhmake can be approximated by the following

```sh
handsdown  --cleanup -o documentation/reference
poetry export -f requirements.txt --output requirements.txt
poetry export -f requirements.txt --with dev --output requirements_optional.txt
poetry build
```

`fhmake audit` can be run to perform additional checks

## Testing

For testing with the version of python used by poetry use

```sh
poetry run pytest
```

Alternatively use `tox` to run tests over python 3.8 - 3.11

```sh
tox
```

## Download Project

### Clone

#### Using The Command Line

1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2

	```bash
	git clone https://github.com/FHPythonUtils/LayeredImage
	```

More information can be found at
https://help.github.com/en/articles/cloning-a-repository

#### Using GitHub Desktop

1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files

### Licence

MIT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog

See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct

Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)
 for more information.

### Contributing

Contributions are welcome, please see the
[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)
for more information.

### Security

Thank you for improving the security of the project, please see the
[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)
for more information.

### Support

Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the
[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)
for more information.

### Rationale

The rationale acts as a guide to various processes regarding projects such as
the versioning scheme and the programming styles used. Please see the
[Rationale](https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md)
for more information.
