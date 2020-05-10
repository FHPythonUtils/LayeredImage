<a name=".layeredimage"></a>
## layeredimage

Use this module to read, and write to a number of layered image formats

<a name=".layeredimage.blend"></a>
## layeredimage.blend

Provide blending functions

leverage blendmodes for this

<a name=".layeredimage.blend.BlendType"></a>
### BlendType

```python
class BlendType(Enum)
```

Specify supported blend types
NORMAL
MULTIPLY
ADDITIVE
COLOURBURN
COLOURDODGE
REFLECT
GLOW
OVERLAY
DIFFERENCE
NEGATION
LIGHTEN
DARKEN
SCREEN
XOR
SOFTLIGHT
HARDLIGHT
GRAINEXTRACT
GRAINMERGE
DIVIDE
HUE
SATURATION
COLOUR
LUMINOSITY
PINLIGHT
VIVIDLIGHT
EXCLUSION
DESTIN
DESTOUT
DESTATOP
SRCATOP

<a name=".layeredimage.blend.blendLayers"></a>
#### blendLayers

```python
blendLayers(background, foreground, blendType, opacity)
```

Blend layers using numpy array

**Arguments**:

- `background` _PIL.Image_ - background layer
- `foreground` _PIL.Image_ - foreground layer
- `blendType` _BlendType_ - The blendtype
- `opacity` _float_ - The opacity of the foreground image
  

**Returns**:

- `PIL.Image` - combined image

<a name=".layeredimage.io"></a>
## layeredimage.io

Do file io

<a name=".layeredimage.io.extNotRecognised"></a>
#### extNotRecognised

```python
extNotRecognised(fileName)
```

Output the file extension not recognised error

<a name=".layeredimage.io.openLayerImage"></a>
#### openLayerImage

```python
openLayerImage(file)
```

Open a layer image file into a layer image object

**Arguments**:

- `file` _string_ - path/ filename
  

**Returns**:

- `LayeredImage` - a layered image object

<a name=".layeredimage.io.saveLayerImage"></a>
#### saveLayerImage

```python
saveLayerImage(fileName, layeredImage)
```

Save a layered image to a file

**Arguments**:

- `fileName` _string_ - path/ filename
- `layeredImage` _LayeredImage_ - the layered image to save

<a name=".layeredimage.io.exportFlatImage"></a>
#### exportFlatImage

```python
exportFlatImage(fileName, layeredImage)
```

Export the layered image to a unilayer image file

<a name=".layeredimage.io.blendModeLookup"></a>
#### blendModeLookup

```python
blendModeLookup(blendmode, blendLookup, default=BlendType.NORMAL)
```

Get the blendmode from a lookup table

<a name=".layeredimage.io.openLayer_ORA"></a>
#### openLayer\_ORA

```python
openLayer_ORA(file)
```

Open an .ora file into a layered image

<a name=".layeredimage.io.saveLayer_ORA"></a>
#### saveLayer\_ORA

```python
saveLayer_ORA(fileName, layeredImage)
```

Save a layered image as .ora

<a name=".layeredimage.io.addLayer_ORA"></a>
#### addLayer\_ORA

```python
addLayer_ORA(project, layer, blendLookup)
```

Update the project with a shiny new layer

<a name=".layeredimage.io.save_ORA_fix"></a>
#### save\_ORA\_fix

```python
save_ORA_fix(path_or_file, composite_image=None, use_original=False)
```

Patch the Project.save function from pyora 3.0 with a newer version -Future
This snippet is MIT License Copyright (c) 2019 Paul Jewell

<a name=".layeredimage.io.openLayer_PSD"></a>
#### openLayer\_PSD

```python
openLayer_PSD(file)
```

Open a .psd file into a layered image

<a name=".layeredimage.io.saveLayer_PSD"></a>
#### saveLayer\_PSD

```python
saveLayer_PSD(_fileName, _layeredImage)
```

Save a layered image as .psd

<a name=".layeredimage.io.openLayer_XCF"></a>
#### openLayer\_XCF

```python
openLayer_XCF(file)
```

Open an .xcf file into a layered image

<a name=".layeredimage.io.saveLayer_XCF"></a>
#### saveLayer\_XCF

```python
saveLayer_XCF(_fileName, _layeredImage)
```

Save a layered image as .xcf

<a name=".layeredimage.io.openLayer_PDN"></a>
#### openLayer\_PDN

```python
openLayer_PDN(file)
```

Open a .pdn file into a layered image

<a name=".layeredimage.io.saveLayer_PDN"></a>
#### saveLayer\_PDN

```python
saveLayer_PDN(_fileName, _layeredImage)
```

Save a layered image as .pdn

<a name=".layeredimage.io.openLayer_TIFF"></a>
#### openLayer\_TIFF

```python
openLayer_TIFF(file)
```

Open a .tiff or a .tif file into a layered image

<a name=".layeredimage.io.saveLayer_TIFF"></a>
#### saveLayer\_TIFF

```python
saveLayer_TIFF(fileName, layeredImage)
```

Save a layered image as .tiff or .tif

<a name=".layeredimage.io.openLayer_GIF"></a>
#### openLayer\_GIF

```python
openLayer_GIF(file)
```

Open a .gif file into a layered image

<a name=".layeredimage.io.saveLayer_GIF"></a>
#### saveLayer\_GIF

```python
saveLayer_GIF(fileName, layeredImage)
```

Save a layered image as .gif

<a name=".layeredimage.io.openLayer_WEBP"></a>
#### openLayer\_WEBP

```python
openLayer_WEBP(file)
```

Open a .webp file into a layered image

<a name=".layeredimage.io.saveLayer_WEBP"></a>
#### saveLayer\_WEBP

```python
saveLayer_WEBP(fileName, layeredImage)
```

Save a layered image as .webp

<a name=".layeredimage.io.getRasterLayers"></a>
#### getRasterLayers

```python
getRasterLayers(layeredImage, imageFormat)
```

Return layers and throw a warning if the image has groups

<a name=".layeredimage.io.openLayer_LSR"></a>
#### openLayer\_LSR

```python
openLayer_LSR(file)
```

Open a .lsr file into a layered image

<a name=".layeredimage.io.saveLayer_LSR"></a>
#### saveLayer\_LSR

```python
saveLayer_LSR(fileName, layeredImage)
```

Save a layered image as .lsr

<a name=".layeredimage.io.openLayer_LAYERED"></a>
#### openLayer\_LAYERED

```python
openLayer_LAYERED(file)
```

Open a .layered file into a layered image

<a name=".layeredimage.io.grabLayer_LAYERED"></a>
#### grabLayer\_LAYERED

```python
grabLayer_LAYERED(zipFile, layer, blendLookup)
```

Grab an image from .layered

<a name=".layeredimage.io.saveLayer_LAYERED"></a>
#### saveLayer\_LAYERED

```python
saveLayer_LAYERED(fileName, layeredImage, compressed=False)
```

Save a layered image as .layered

<a name=".layeredimage.io.writeImage_LAYERED"></a>
#### writeImage\_LAYERED

```python
writeImage_LAYERED(image, zipFile, path, compressed=False)
```

Write an image to the archive

<a name=".layeredimage.io.openLayer_LAYEREDC"></a>
#### openLayer\_LAYEREDC

```python
openLayer_LAYEREDC(file)
```

Open a .layeredc file into a layered image

<a name=".layeredimage.io.saveLayer_LAYEREDC"></a>
#### saveLayer\_LAYEREDC

```python
saveLayer_LAYEREDC(fileName, layeredImage)
```

Save a layeredc image as .layered

<a name=".layeredimage.layeredimage"></a>
## layeredimage.layeredimage

LayeredImage class

<a name=".layeredimage.layeredimage.LayeredImage"></a>
### LayeredImage

```python
class LayeredImage()
```

A representation of a layered image such as an ora

<a name=".layeredimage.layeredimage.LayeredImage.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(layersAndGroups, dimensions=None, **kwargs)
```

Write here

<a name=".layeredimage.layeredimage.LayeredImage.json"></a>
#### json

```python
 | json()
```

Get the object as a dict

<a name=".layeredimage.layeredimage.LayeredImage.getLayerOrGroup"></a>
#### getLayerOrGroup

```python
 | getLayerOrGroup(index)
```

Get a LayerOrGroup

<a name=".layeredimage.layeredimage.LayeredImage.addLayerOrGroup"></a>
#### addLayerOrGroup

```python
 | addLayerOrGroup(LayerOrGroup)
```

Add a LayerOrGroup

<a name=".layeredimage.layeredimage.LayeredImage.insertLayerOrGroup"></a>
#### insertLayerOrGroup

```python
 | insertLayerOrGroup(LayerOrGroup, index)
```

Insert a LayerOrGroup at a specific index

<a name=".layeredimage.layeredimage.LayeredImage.removeLayerOrGroup"></a>
#### removeLayerOrGroup

```python
 | removeLayerOrGroup(index)
```

Remove a LayerOrGroup at a specific index

<a name=".layeredimage.layeredimage.LayeredImage.addLayerRaster"></a>
#### addLayerRaster

```python
 | addLayerRaster(image, name)
```

Raster an image and add as a layer

<a name=".layeredimage.layeredimage.LayeredImage.insertLayerRaster"></a>
#### insertLayerRaster

```python
 | insertLayerRaster(image, name, index)
```

Raster an image and insert the layer

<a name=".layeredimage.layeredimage.LayeredImage.getFlattenLayers"></a>
#### getFlattenLayers

```python
 | getFlattenLayers(ignoreHidden=True)
```

Return an image for all flattened layers

<a name=".layeredimage.layeredimage.LayeredImage.getFlattenTwoLayers"></a>
#### getFlattenTwoLayers

```python
 | getFlattenTwoLayers(background, foreground, ignoreHidden=True)
```

Return an image for two flattened layers

<a name=".layeredimage.layeredimage.LayeredImage.flattenTwoLayers"></a>
#### flattenTwoLayers

```python
 | flattenTwoLayers(background, foreground, ignoreHidden=True)
```

Flatten two layers

<a name=".layeredimage.layeredimage.LayeredImage.flattenLayers"></a>
#### flattenLayers

```python
 | flattenLayers(ignoreHidden=True)
```

Flatten all layers

<a name=".layeredimage.layeredimage.LayeredImage.extractLayers"></a>
#### extractLayers

```python
 | extractLayers()
```

Extract the layers from the image

<a name=".layeredimage.layeredimage.LayeredImage.updateLayers"></a>
#### updateLayers

```python
 | updateLayers()
```

Update the layers from the image

<a name=".layeredimage.layeredimage.LayeredImage.extractGroups"></a>
#### extractGroups

```python
 | extractGroups()
```

Extract the groups from the image

<a name=".layeredimage.layeredimage.LayeredImage.updateGroups"></a>
#### updateGroups

```python
 | updateGroups()
```

Update the groups from the image

<a name=".layeredimage.layeredimage.rasterImageOA"></a>
#### rasterImageOA

```python
rasterImageOA(image, size, alpha=1.0, offsets=(0, 0))
```

Rasterise an image with offset and alpha to a given size

<a name=".layeredimage.layeredimage.rasterImageOffset"></a>
#### rasterImageOffset

```python
rasterImageOffset(image, size, offsets=(0, 0))
```

Rasterise an image with offset to a given size

<a name=".layeredimage.layeredimage.flattenLayerOrGroup"></a>
#### flattenLayerOrGroup

```python
flattenLayerOrGroup(layerOrGroup, imageDimensions, flattenedSoFar=None, ignoreHidden=True)
```

Flatten a layer or group on to an image of what has already been
flattened

**Arguments**:

- `layerOrGroup` _Layer|Group_ - A layer or a group of layers
  imageDimensions ((int, int)): size of the image
- `flattenedSoFar` _PIL.Image, optional_ - the image of what has already
  been flattened. Defaults to None.
- `ignoreHidden` _bool, optional_ - ignore layers that are hidden. Defaults
  to True.
  

**Returns**:

- `PIL.Image` - Flattened image

<a name=".layeredimage.layeredimage.flattenAll"></a>
#### flattenAll

```python
flattenAll(layers, imageDimensions, ignoreHidden)
```

Flatten a list of layers and groups

**Arguments**:

- `layers` _[Layer|Group]_ - A list of layers and groups
  imageDimensions ((int, int)): size of the image
  been flattened. Defaults to None.
- `ignoreHidden` _bool, optional_ - ignore layers that are hidden. Defaults
  to True.
  

**Returns**:

- `PIL.Image` - Flattened image

<a name=".layeredimage.layergrou"></a>
## layeredimage.layergrou

Base class

<a name=".layeredimage.layergrou.LayerGroupTypes"></a>
### LayerGroupTypes

```python
class LayerGroupTypes(Enum)
```

Can be a LAYER, GROUP, or UNDEFINED

<a name=".layeredimage.layergrou.LayerGroup"></a>
### LayerGroup

```python
class LayerGroup()
```

A representation of an image layer or group

<a name=".layeredimage.layergrou.LayerGroup.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(name, dimensions, offsets=(0, 0), opacity=1.0, visible=True, layerGroup=LayerGroupTypes.LAYER, blendmode=BlendType.NORMAL, **kwargs)
```

A representation of an image layer or group

**Arguments**:

- `name` _string_ - Name of the layer or group
  dimensions ((int, int)): A tuple representing the dimentions in
  pixels
- `offsets` _tuple, optional_ - A tuple representing the left and top
  offsets in pixels. Defaults to (0, 0).
- `opacity` _float, optional_ - A float representing the alpha value
  where 0 is invisible and 1 is fully visible. Defaults to 1.0.
- `visible` _bool, optional_ - Is the layer visible to the user (this
  is often configured per layer or per group by an 'eye' icon).
  Defaults to True.
- `layerGroup` _[type], optional_ - Type LAYER, GROUP, or UNDEFINED.
  Defaults to LayerGroupTypes.LAYER.

<a name=".layeredimage.layergrou.Layer"></a>
### Layer

```python
class Layer(LayerGroup)
```

A representation of an image layer

<a name=".layeredimage.layergrou.Layer.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(name, image, dimensions=None, offsets=(0, 0), opacity=1.0, visible=True, blendmode=BlendType.NORMAL)
```

A representation of an image layer

**Arguments**:

- `name` _string_ - Name of the layer or group
- `image` _PIL.Image_ - A PIL Image
  dimensions ((int, int)): A tuple representing the dimentions in
  pixels
- `offsets` _tuple, optional_ - A tuple representing the left and top
  offsets in pixels. Defaults to (0, 0).
- `opacity` _float, optional_ - A float representing the alpha value
  where 0 is invisible and 1 is fully visible. Defaults to 1.0.
- `visible` _bool, optional_ - Is the layer visible to the user (this
  is often configured per layer or per group by an 'eye' icon).
  Defaults to True.

<a name=".layeredimage.layergrou.Layer.json"></a>
#### json

```python
 | json()
```

Get the object as a dict

<a name=".layeredimage.layergrou.Group"></a>
### Group

```python
class Group(LayerGroup)
```

A representation of an image group

<a name=".layeredimage.layergrou.Group.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(name, layers, dimensions=None, offsets=(0, 0), opacity=1.0, visible=True, blendmode=BlendType.NORMAL)
```

A representation of an image group

**Arguments**:

- `name` _string_ - Name of the layer or group
- `layers` _layeredimage.Layer[]_ - A list of layers where the next
  index stacks upon the previous layer
  dimensions ((int, int)): A tuple representing the dimentions in
  pixels
- `offsets` _tuple, optional_ - A tuple representing the left and top
  offsets in pixels. Defaults to (0, 0).
- `opacity` _float, optional_ - A float representing the alpha value
  where 0 is invisible and 1 is fully visible. Defaults to 1.0.
- `visible` _bool, optional_ - Is the layer visible to the user (this
  is often configured per layer or per group by an 'eye' icon).
  Defaults to True.

<a name=".layeredimage.layergrou.Group.json"></a>
#### json

```python
 | json()
```

Get the object as a dict

<a name=".make"></a>
## make

Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build

