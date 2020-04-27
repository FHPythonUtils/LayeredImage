[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/LayeredImage.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/[codacy-proj-id].svg?style=for-the-badge)](https://www.codacy.com/manual/FHPythonUtils/LayeredImage)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/LayeredImage.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/LayeredImage.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/LayeredImage.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/LayeredImage.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/LayeredImage.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/layeredimage.svg?style=for-the-badge)](https://pypi.org/project/layeredimage/)
[![PyPI Version](https://img.shields.io/pypi/v/layeredimage.svg?style=for-the-badge)](https://pypi.org/project/layeredimage/)

<!-- omit in TOC -->
# LayeredImage

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Use this module to read, and write to a number of layered image formats

- [Compatibility](#compatibility)
	- [Overview](#overview)
		- [Key](#key)
	- [Reading](#reading)
		- [Group](#group)
		- [Layer](#layer)
	- [Writing](#writing)
		- [Group](#group-1)
		- [Layer](#layer-1)
- [Docs](#docs)
- [Example Usage](#example-usage)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Download](#download)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
- [How to run](#how-to-run)
	- [With VSCode](#with-vscode)
	- [From the Terminal](#from-the-terminal)
- [How to update, build and publish](#how-to-update-build-and-publish)
- [Download](#download-1)
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

## Compatibility

Bear in mind that the tables below may not be completely accurate. If that is
the case, please open an issue and I will fix the tables.

### Overview

#### Key
- :heavy_check_mark: - Supported
- :warning: - Things will look the same, but data is lost
- :x: - This is not supported and will cause loss of data
- N/A - The source format does not support this so treat this as a :heavy_check_mark:

|Format|.ora|.pdn|.xcf|.psd|.tiff/ .tif|.webp|.gif|
|------|----|----|----|----|-----|----|-----|
|Read  |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|Layers|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|Groups|:heavy_check_mark:|N/A |:heavy_check_mark:|:heavy_check_mark:|N/A|N/A|N/A|
|Write |:heavy_check_mark:|:x:  |:x:  |:x:  |:warning:|:warning:|:warning:|

### Reading

#### Group

|Format    |.ora|.pdn|.xcf|.psd|.tiff/ .tif|.webp|.gif|
|----------|----|----|----|----|-----|----|-----|
|Name      |:heavy_check_mark:|N/A |:heavy_check_mark:|:heavy_check_mark:|N/A |N/A |N/A |
|Dimensions|:warning:|N/A |:heavy_check_mark:|:heavy_check_mark:|N/A |N/A |N/A |
|Offsets   |:heavy_check_mark:|N/A |:heavy_check_mark:|:heavy_check_mark:|N/A |N/A |N/A |
|Opacity   |:heavy_check_mark:|N/A |:heavy_check_mark:|:heavy_check_mark:|N/A |N/A |N/A |
|Visibility|:heavy_check_mark:|N/A |:x:  |:heavy_check_mark:|N/A |N/A |N/A |
|Blend Mode|:heavy_check_mark:|N/A |:heavy_check_mark:|:heavy_check_mark:|N/A|N/A |N/A |

#### Layer

|Format    |.ora|.pdn|.xcf|.psd|.tiff/ .tif|.webp|.gif|
|----------|----|----|----|----|-----|----|-----|
|Name      |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:warning:|:warning:|
|Dimensions|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
|Offsets   |:heavy_check_mark:|N/A |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|N/A|N/A|
|Opacity   |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|N/A |N/A |N/A |
|Visibility|:heavy_check_mark:|:heavy_check_mark:|:x:  |:heavy_check_mark:|N/A |N/A |N/A |
|Blend Mode|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|N/A|N/A |N/A |

### Writing

#### Group

|Format    |.ora|.pdn|.xcf|.psd|.tiff/ .tif|.webp|.gif|
|----------|----|----|----|----|-----|----|-----|
|Name      |:heavy_check_mark:|:x:|:x:|:x:|:x:|:x:|:x:|
|Dimensions|:heavy_check_mark:|:x:|:x:|:x:|:warning:|:warning:|:warning:|
|Offsets   |:heavy_check_mark:|:x:|:x:|:x:|:warning:|:warning:|:warning:|
|Opacity   |:heavy_check_mark:|:x:|:x:|:x:|:warning:|:warning:|:warning:|
|Visibility|:heavy_check_mark:|:x:|:x:|:x:|:warning:|:warning:|:warning:|
|Blend Mode|:heavy_check_mark:|:x:|:x:|:x:|:x:|:x:|:x:|

```none
Layers are extracted from groups and saved to TIFF/ GIF or WEBP
```

#### Layer

|Format    |.ora|.pdn|.xcf|.psd|.tiff/ .tif|.webp|.gif|
|----------|----|----|----|----|-----|----|-----|
|Name      |:heavy_check_mark:|:x:|:x:|:x:|:x:|:x:|:x:|
|Dimensions|:heavy_check_mark:|:x:|:x:|:x:|:warning:|:warning:|:warning:|
|Offsets   |:heavy_check_mark:|:x:|:x:|:x:|:warning:|:warning:|:warning:|
|Opacity   |:heavy_check_mark:|:x:|:x:|:x:|:warning:|:warning:|:warning:|
|Visibility|:heavy_check_mark:|:x:|:x:|:x:|:warning:|:warning:|:warning:|
|Blend Mode|:heavy_check_mark:|:x:|:x:|:x:|:x:|:x:|:x:|

```none
Layers are rasterized before being written to TIFF/ GIF or WEBP
```

## Docs
See the [Docs](/DOCS.md) for more information.

Generate with pydoc-markdown 3
```bash
pydoc-markdown > DOCS.md
```

## Example Usage

Here's some basic example usage below.

```python
"""Example module """
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
import layeredimage.io

# Do stuff
ora = layeredimage.io.openLayerImage(THISDIR + "/image.ora")

imageDimensions = ora.dimensions
# There are a load of handy functions for getting layers, and adding new
# layers, but here we will act directly on the object
layer = ora.layersAndGroups[0] # For the sake of the e.g. this is a layer

# Lets overwrite the layer with a transparent image (bit boring I know...)
layer.image = Image.new("RGBA", imageDimensions)
ora.layersAndGroups[0] = layer

# And let's save
layeredimage.io.saveLayerImage(THISDIR + "/image(modified).ora", ora)

# Let's save a flattened version too
ora.getFlattenLayers().save(THISDIR + "/image(modified).png")

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
```

## Install With PIP

```python
pip install layeredimage
```

Head to https://pypi.org/project/layeredimage/ for more info


## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.8.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.8
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.8 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.8)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```

## How to update, build and publish

1. Ensure you have installed the following dependencies
	Linux
	```bash
	wget dephell.org/install | python3.8
	wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.8
	```
	Windows
	```powershell
	(wget dephell.org/install -UseBasicParsing).Content | python
	(wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
	```
2. Use poetry for the heavy lifting and dephell to generate requirements
	```bash
	poetry update
	dephell deps convert
	```
3. Build/ Publish
	```bash
	poetry build
	poetry publish
	```
	or
	```bash
	poetry publish --build
	```


## Download
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/FHPythonUtils/LayeredImage
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

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
In the interest of fostering an open and welcoming environment, we
as contributors and maintainers pledge to make participation in our
project and our community a harassment-free experience for everyone.
Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md) for more information.

### Contributing
Contributions are welcome, please see the [Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md) for more information.

### Security
Thank you for improving the security of the project, please see the [Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md) for more information.
