# LayeredImage

[Layeredimage Index](../README.md#layeredimage-index) /
[Layeredimage](./index.md#layeredimage) /
LayeredImage

> Auto-generated documentation for [layeredimage.layeredimage](../../../layeredimage/layeredimage.py) module.

- [LayeredImage](#layeredimage)
  - [LayeredImage](#layeredimage-1)
    - [LayeredImage().__repr__](#layeredimage()__repr__)
    - [LayeredImage().__str__](#layeredimage()__str__)
    - [LayeredImage().addImageAsLayer](#layeredimage()addimageaslayer)
    - [LayeredImage().addLayerOrGroup](#layeredimage()addlayerorgroup)
    - [LayeredImage().addLayerRaster](#layeredimage()addlayerraster)
    - [LayeredImage().extractGroups](#layeredimage()extractgroups)
    - [LayeredImage().extractLayers](#layeredimage()extractlayers)
    - [LayeredImage().flattenLayers](#layeredimage()flattenlayers)
    - [LayeredImage().flattenTwoLayers](#layeredimage()flattentwolayers)
    - [LayeredImage().getFlattenLayers](#layeredimage()getflattenlayers)
    - [LayeredImage().getFlattenTwoLayers](#layeredimage()getflattentwolayers)
    - [LayeredImage().getLayerOrGroup](#layeredimage()getlayerorgroup)
    - [LayeredImage().insertImageAsLayer](#layeredimage()insertimageaslayer)
    - [LayeredImage().insertLayerOrGroup](#layeredimage()insertlayerorgroup)
    - [LayeredImage().insertLayerRaster](#layeredimage()insertlayerraster)
    - [LayeredImage().json](#layeredimage()json)
    - [LayeredImage().removeLayerOrGroup](#layeredimage()removelayerorgroup)
    - [LayeredImage().updateGroups](#layeredimage()updategroups)
    - [LayeredImage().updateLayers](#layeredimage()updatelayers)
  - [flattenAll](#flattenall)
  - [flattenLayerOrGroup](#flattenlayerorgroup)

## LayeredImage

[Show source in layeredimage.py:15](../../../layeredimage/layeredimage.py#L15)

A representation of a layered image such as an ora.

#### Signature

```python
class LayeredImage:
    def __init__(
        self,
        layersAndGroups: list[Layer | Group],
        dimensions: tuple[int, int] | None = None,
        **kwargs: Any
    ):
        ...
```

### LayeredImage().__repr__

[Show source in layeredimage.py:46](../../../layeredimage/layeredimage.py#L46)

Get the string representation.

#### Signature

```python
def __repr__(self):
    ...
```

### LayeredImage().__str__

[Show source in layeredimage.py:50](../../../layeredimage/layeredimage.py#L50)

Get the string representation.

#### Signature

```python
def __str__(self):
    ...
```

### LayeredImage().addImageAsLayer

[Show source in layeredimage.py:91](../../../layeredimage/layeredimage.py#L91)

Resize an image to the canvas and add as a layer.

#### Signature

```python
def addImageAsLayer(self, image: Image.Image, name: str):
    ...
```

### LayeredImage().addLayerOrGroup

[Show source in layeredimage.py:72](../../../layeredimage/layeredimage.py#L72)

Add a LayerOrGroup.

#### Signature

```python
def addLayerOrGroup(self, layerOrGroup: Layer | Group):
    ...
```

### LayeredImage().addLayerRaster

[Show source in layeredimage.py:85](../../../layeredimage/layeredimage.py#L85)

#### Signature

```python
@deprecated(details="use addImageAsLayer", deprecated_in="2021.2.4")
def addLayerRaster(self, image: Image.Image, name: str):
    ...
```

### LayeredImage().extractGroups

[Show source in layeredimage.py:176](../../../layeredimage/layeredimage.py#L176)

Extract the groups from the image.

#### Signature

```python
def extractGroups(self):
    ...
```

### LayeredImage().extractLayers

[Show source in layeredimage.py:145](../../../layeredimage/layeredimage.py#L145)

Extract the layers from the image.

#### Signature

```python
def extractLayers(self):
    ...
```

### LayeredImage().flattenLayers

[Show source in layeredimage.py:134](../../../layeredimage/layeredimage.py#L134)

Flatten all layers.

#### Signature

```python
def flattenLayers(self, ignoreHidden: bool = True):
    ...
```

### LayeredImage().flattenTwoLayers

[Show source in layeredimage.py:126](../../../layeredimage/layeredimage.py#L126)

Flatten two layers.

#### Signature

```python
def flattenTwoLayers(self, background: int, foreground: int, ignoreHidden: bool = True):
    ...
```

### LayeredImage().getFlattenLayers

[Show source in layeredimage.py:108](../../../layeredimage/layeredimage.py#L108)

Return an image for all flattened layers.

#### Signature

```python
def getFlattenLayers(self, ignoreHidden: bool = True) -> Image.Image:
    ...
```

### LayeredImage().getFlattenTwoLayers

[Show source in layeredimage.py:112](../../../layeredimage/layeredimage.py#L112)

Return an image for two flattened layers.

#### Signature

```python
def getFlattenTwoLayers(
    self, background: int, foreground: int, ignoreHidden: bool = True
) -> Image.Image:
    ...
```

### LayeredImage().getLayerOrGroup

[Show source in layeredimage.py:68](../../../layeredimage/layeredimage.py#L68)

Get a LayerOrGroup.

#### Signature

```python
def getLayerOrGroup(self, index: int):
    ...
```

### LayeredImage().insertImageAsLayer

[Show source in layeredimage.py:102](../../../layeredimage/layeredimage.py#L102)

Resize an image to the canvas  and insert the layer.

#### Signature

```python
def insertImageAsLayer(self, image: Image.Image, name: str, index: int):
    ...
```

### LayeredImage().insertLayerOrGroup

[Show source in layeredimage.py:76](../../../layeredimage/layeredimage.py#L76)

Insert a LayerOrGroup at a specific index.

#### Signature

```python
def insertLayerOrGroup(self, layerOrGroup: Layer | Group, index: int):
    ...
```

### LayeredImage().insertLayerRaster

[Show source in layeredimage.py:96](../../../layeredimage/layeredimage.py#L96)

#### Signature

```python
@deprecated(details="use insertImageAsLayer", deprecated_in="2021.2.4")
def insertLayerRaster(self, image: Image.Image, name: str, index: int):
    ...
```

### LayeredImage().json

[Show source in layeredimage.py:62](../../../layeredimage/layeredimage.py#L62)

Get the object as a dict.

#### Signature

```python
def json(self) -> dict[str, Any]:
    ...
```

### LayeredImage().removeLayerOrGroup

[Show source in layeredimage.py:80](../../../layeredimage/layeredimage.py#L80)

Remove a LayerOrGroup at a specific index.

#### Signature

```python
def removeLayerOrGroup(self, index: int):
    ...
```

### LayeredImage().updateGroups

[Show source in layeredimage.py:184](../../../layeredimage/layeredimage.py#L184)

Update the groups from the image.

#### Signature

```python
def updateGroups(self):
    ...
```

### LayeredImage().updateLayers

[Show source in layeredimage.py:172](../../../layeredimage/layeredimage.py#L172)

Update the layers from the image.

#### Signature

```python
def updateLayers(self):
    ...
```



## flattenAll

[Show source in layeredimage.py:229](../../../layeredimage/layeredimage.py#L229)

Flatten a list of layers and groups.

#### Arguments

layers (list[Layer | Group] | list[Layer]): A list of layers and groups
imageDimensions (tuple[int, int]): size of the image
been flattened. Defaults to None.
- `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
to True.

#### Returns

- `Image.Image` - Flattened image

#### Signature

```python
def flattenAll(
    layers: list[Layer | Group] | list[Layer],
    imageDimensions: tuple[int, int],
    ignoreHidden: bool = True,
):
    ...
```



## flattenLayerOrGroup

[Show source in layeredimage.py:189](../../../layeredimage/layeredimage.py#L189)

Flatten a layer or group on to an image of what has already been flattened.

#### Arguments

layerOrGroup (Layer, Group): A layer or a group of layers
imageDimensions (tuple[int, int]): size of the image
- `flattenedSoFar` *Image.Image, optional* - the image of what has already
been flattened. Defaults to None.
- `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
to True.

#### Returns

- `Image.Image` - Flattened image

#### Signature

```python
def flattenLayerOrGroup(
    layerOrGroup: Layer | Group,
    imageDimensions: tuple[int, int],
    flattenedSoFar: Image.Image | None = None,
    ignoreHidden: bool = True,
):
    ...
```


