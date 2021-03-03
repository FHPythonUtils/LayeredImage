# layeredimage

> Auto-generated documentation for [layeredimage.layeredimage](../../layeredimage/layeredimage.py) module.

LayeredImage class.

- [Layeredimage](../README.md#layeredimage-index) / [Modules](../README.md#layeredimage-modules) / [layeredimage](index.md#layeredimage) / layeredimage
    - [LayeredImage](#layeredimage)
        - [LayeredImage().\_\_repr\_\_](#layeredimage__repr__)
        - [LayeredImage().\_\_str\_\_](#layeredimage__str__)
        - [LayeredImage().addLayerOrGroup](#layeredimageaddlayerorgroup)
        - [LayeredImage().addLayerRaster](#layeredimageaddlayerraster)
        - [LayeredImage().extractGroups](#layeredimageextractgroups)
        - [LayeredImage().extractLayers](#layeredimageextractlayers)
        - [LayeredImage().flattenLayers](#layeredimageflattenlayers)
        - [LayeredImage().flattenTwoLayers](#layeredimageflattentwolayers)
        - [LayeredImage().getFlattenLayers](#layeredimagegetflattenlayers)
        - [LayeredImage().getFlattenTwoLayers](#layeredimagegetflattentwolayers)
        - [LayeredImage().getLayerOrGroup](#layeredimagegetlayerorgroup)
        - [LayeredImage().insertLayerOrGroup](#layeredimageinsertlayerorgroup)
        - [LayeredImage().insertLayerRaster](#layeredimageinsertlayerraster)
        - [LayeredImage().json](#layeredimagejson)
        - [LayeredImage().removeLayerOrGroup](#layeredimageremovelayerorgroup)
        - [LayeredImage().updateGroups](#layeredimageupdategroups)
        - [LayeredImage().updateLayers](#layeredimageupdatelayers)
    - [flattenAll](#flattenall)
    - [flattenLayerOrGroup](#flattenlayerorgroup)
    - [rasterImageOA](#rasterimageoa)
    - [rasterImageOffset](#rasterimageoffset)

## LayeredImage

[[find in source code]](../../layeredimage/layeredimage.py#L12)

```python
class LayeredImage():
    def __init__(
        layersAndGroups: list[Layer | Group],
        dimensions: tuple[(int, int)] | None = None,
        **kwargs: Any,
    ):
```

A representation of a layered image such as an ora.

### LayeredImage().\_\_repr\_\_

[[find in source code]](../../layeredimage/layeredimage.py#L32)

```python
def __repr__():
```

Get the string representation.

### LayeredImage().\_\_str\_\_

[[find in source code]](../../layeredimage/layeredimage.py#L36)

```python
def __str__():
```

Get the string representation.

### LayeredImage().addLayerOrGroup

[[find in source code]](../../layeredimage/layeredimage.py#L52)

```python
def addLayerOrGroup(layerOrGroup: Layer | Group):
```

Add a LayerOrGroup.

### LayeredImage().addLayerRaster

[[find in source code]](../../layeredimage/layeredimage.py#L65)

```python
def addLayerRaster(image: Image.Image, name: str):
```

Raster an image and add as a layer.

### LayeredImage().extractGroups

[[find in source code]](../../layeredimage/layeredimage.py#L140)

```python
def extractGroups():
```

Extract the groups from the image.

### LayeredImage().extractLayers

[[find in source code]](../../layeredimage/layeredimage.py#L116)

```python
def extractLayers():
```

Extract the layers from the image.

### LayeredImage().flattenLayers

[[find in source code]](../../layeredimage/layeredimage.py#L105)

```python
def flattenLayers(ignoreHidden: bool = True):
```

Flatten all layers.

### LayeredImage().flattenTwoLayers

[[find in source code]](../../layeredimage/layeredimage.py#L93)

```python
def flattenTwoLayers(
    background: int,
    foreground: int,
    ignoreHidden: bool = True,
):
```

Flatten two layers.

### LayeredImage().getFlattenLayers

[[find in source code]](../../layeredimage/layeredimage.py#L76)

```python
def getFlattenLayers(ignoreHidden: bool = True) -> Image.Image:
```

Return an image for all flattened layers.

### LayeredImage().getFlattenTwoLayers

[[find in source code]](../../layeredimage/layeredimage.py#L80)

```python
def getFlattenTwoLayers(
    background: int,
    foreground: int,
    ignoreHidden: bool = True,
) -> Image.Image:
```

Return an image for two flattened layers.

### LayeredImage().getLayerOrGroup

[[find in source code]](../../layeredimage/layeredimage.py#L48)

```python
def getLayerOrGroup(index: int):
```

Get a LayerOrGroup.

### LayeredImage().insertLayerOrGroup

[[find in source code]](../../layeredimage/layeredimage.py#L56)

```python
def insertLayerOrGroup(layerOrGroup: Layer | Group, index: int):
```

Insert a LayerOrGroup at a specific index.

### LayeredImage().insertLayerRaster

[[find in source code]](../../layeredimage/layeredimage.py#L70)

```python
def insertLayerRaster(image: Image.Image, name: str, index: int):
```

Raster an image and insert the layer.

### LayeredImage().json

[[find in source code]](../../layeredimage/layeredimage.py#L41)

```python
def json() -> dict[(str, Any)]:
```

Get the object as a dict.

### LayeredImage().removeLayerOrGroup

[[find in source code]](../../layeredimage/layeredimage.py#L60)

```python
def removeLayerOrGroup(index: int):
```

Remove a LayerOrGroup at a specific index.

### LayeredImage().updateGroups

[[find in source code]](../../layeredimage/layeredimage.py#L146)

```python
def updateGroups():
```

Update the groups from the image.

### LayeredImage().updateLayers

[[find in source code]](../../layeredimage/layeredimage.py#L136)

```python
def updateLayers():
```

Update the layers from the image.

## flattenAll

[[find in source code]](../../layeredimage/layeredimage.py#L206)

```python
def flattenAll(
    layers: list[Layer | Group] | list[Layer],
    imageDimensions: tuple[(int, int)],
    ignoreHidden: bool = True,
):
```

Flatten a list of layers and groups.

#### Arguments

layers (list[Layer | Group] | list[Layer]): A list of layers and groups
imageDimensions (tuple[int, int]): size of the image
been flattened. Defaults to None.
- `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
to True.

#### Returns

- `Image.Image` - Flattened image

## flattenLayerOrGroup

[[find in source code]](../../layeredimage/layeredimage.py#L169)

```python
def flattenLayerOrGroup(
    layerOrGroup: Layer | Group,
    imageDimensions: tuple[(int, int)],
    flattenedSoFar: Image.Image | None = None,
    ignoreHidden: bool = True,
):
```

Flatten a layer or group on to an image of what has already been flattened.

#### Arguments

layerOrGroup (Layer | Group): A layer or a group of layers
imageDimensions (tuple[int, int]): size of the image
- `flattenedSoFar` *Image.Image, optional* - the image of what has already
been flattened. Defaults to None.
- `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
to True.

#### Returns

- `Image.Image` - Flattened image

## rasterImageOA

[[find in source code]](../../layeredimage/layeredimage.py#L151)

```python
def rasterImageOA(
    image: Image.Image,
    size: tuple[(int, int)],
    alpha: float = 1.0,
    offsets: tuple[(int, int)] = (0, 0),
):
```

Rasterise an image with offset and alpha to a given size.

## rasterImageOffset

[[find in source code]](../../layeredimage/layeredimage.py#L160)

```python
def rasterImageOffset(
    image: Image.Image,
    size: tuple[(int, int)],
    offsets: tuple[(int, int)] = (0, 0),
):
```

Rasterise an image with offset to a given size.
