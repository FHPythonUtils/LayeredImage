# LayeredImage

[Layeredimage Index](../README.md#layeredimage-index) / [Layeredimage](./index.md#layeredimage) / LayeredImage

> Auto-generated documentation for [layeredimage.layeredimage](../../../layeredimage/layeredimage.py) module.

- [LayeredImage](#layeredimage)
  - [LayeredImage](#layeredimage-1)
    - [LayeredImage().__repr__](#layeredimage()__repr__)
    - [LayeredImage().__str__](#layeredimage()__str__)
    - [LayeredImage().addImageAsLayer](#layeredimage()addimageaslayer)
    - [LayeredImage().addLayerOrGroup](#layeredimage()addlayerorgroup)
    - [LayeredImage().extractGroups](#layeredimage()extractgroups)
    - [LayeredImage().extractLayers](#layeredimage()extractlayers)
    - [LayeredImage().flattenLayers](#layeredimage()flattenlayers)
    - [LayeredImage().flattenTwoLayers](#layeredimage()flattentwolayers)
    - [LayeredImage().getFlattenLayers](#layeredimage()getflattenlayers)
    - [LayeredImage().getFlattenTwoLayers](#layeredimage()getflattentwolayers)
    - [LayeredImage().getLayerOrGroup](#layeredimage()getlayerorgroup)
    - [LayeredImage().insertImageAsLayer](#layeredimage()insertimageaslayer)
    - [LayeredImage().insertLayerOrGroup](#layeredimage()insertlayerorgroup)
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
    ) -> None: ...
```

### LayeredImage().__repr__

[Show source in layeredimage.py:48](../../../layeredimage/layeredimage.py#L48)

Get the string representation.

#### Signature

```python
def __repr__(self) -> str: ...
```

### LayeredImage().__str__

[Show source in layeredimage.py:52](../../../layeredimage/layeredimage.py#L52)

Get the string representation.

#### Signature

```python
def __str__(self) -> str: ...
```

### LayeredImage().addImageAsLayer

[Show source in layeredimage.py:86](../../../layeredimage/layeredimage.py#L86)

Resize an image to the canvas and add as a layer.

#### Signature

```python
def addImageAsLayer(self, image: Image.Image, name: str) -> None: ...
```

### LayeredImage().addLayerOrGroup

[Show source in layeredimage.py:74](../../../layeredimage/layeredimage.py#L74)

Add a LayerOrGroup.

#### Signature

```python
def addLayerOrGroup(self, layerOrGroup: Layer | Group) -> None: ...
```

### LayeredImage().extractGroups

[Show source in layeredimage.py:171](../../../layeredimage/layeredimage.py#L171)

Extract the groups from the image.

#### Signature

```python
def extractGroups(self) -> list[Group]: ...
```

### LayeredImage().extractLayers

[Show source in layeredimage.py:140](../../../layeredimage/layeredimage.py#L140)

Extract the layers from the image.

#### Signature

```python
def extractLayers(self) -> list[Layer]: ...
```

### LayeredImage().flattenLayers

[Show source in layeredimage.py:129](../../../layeredimage/layeredimage.py#L129)

Flatten all layers.

#### Signature

```python
def flattenLayers(self, ignoreHidden: bool = True) -> None: ...
```

### LayeredImage().flattenTwoLayers

[Show source in layeredimage.py:119](../../../layeredimage/layeredimage.py#L119)

Flatten two layers.

#### Signature

```python
def flattenTwoLayers(
    self, background: int, foreground: int, ignoreHidden: bool = True
) -> None: ...
```

### LayeredImage().getFlattenLayers

[Show source in layeredimage.py:97](../../../layeredimage/layeredimage.py#L97)

Return an image for all flattened layers.

#### Signature

```python
def getFlattenLayers(self, ignoreHidden: bool = True) -> Image.Image: ...
```

### LayeredImage().getFlattenTwoLayers

[Show source in layeredimage.py:101](../../../layeredimage/layeredimage.py#L101)

Return an image for two flattened layers.

#### Signature

```python
def getFlattenTwoLayers(
    self, background: int, foreground: int, ignoreHidden: bool = True
) -> Image.Image: ...
```

### LayeredImage().getLayerOrGroup

[Show source in layeredimage.py:70](../../../layeredimage/layeredimage.py#L70)

Get a LayerOrGroup.

#### Signature

```python
def getLayerOrGroup(self, index: int) -> Layer | Group: ...
```

### LayeredImage().insertImageAsLayer

[Show source in layeredimage.py:91](../../../layeredimage/layeredimage.py#L91)

Resize an image to the canvas  and insert the layer.

#### Signature

```python
def insertImageAsLayer(self, image: Image.Image, name: str, index: int) -> None: ...
```

### LayeredImage().insertLayerOrGroup

[Show source in layeredimage.py:78](../../../layeredimage/layeredimage.py#L78)

Insert a LayerOrGroup at a specific index.

#### Signature

```python
def insertLayerOrGroup(self, layerOrGroup: Layer | Group, index: int) -> None: ...
```

### LayeredImage().json

[Show source in layeredimage.py:64](../../../layeredimage/layeredimage.py#L64)

Get the object as a dict.

#### Signature

```python
def json(self) -> dict[str, Any]: ...
```

### LayeredImage().removeLayerOrGroup

[Show source in layeredimage.py:82](../../../layeredimage/layeredimage.py#L82)

Remove a LayerOrGroup at a specific index.

#### Signature

```python
def removeLayerOrGroup(self, index: int) -> None: ...
```

### LayeredImage().updateGroups

[Show source in layeredimage.py:179](../../../layeredimage/layeredimage.py#L179)

Update the groups from the image.

#### Signature

```python
def updateGroups(self) -> None: ...
```

### LayeredImage().updateLayers

[Show source in layeredimage.py:167](../../../layeredimage/layeredimage.py#L167)

Update the layers from the image.

#### Signature

```python
def updateLayers(self) -> None: ...
```



## flattenAll

[Show source in layeredimage.py:227](../../../layeredimage/layeredimage.py#L227)

Flatten a list of layers and groups.

#### Arguments

----
 layers (list[Layer | Group] | list[Layer]): A list of layers and groups
 imageDimensions (tuple[int, int]): size of the image
 been flattened. Defaults to None.
 - `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
 to True.

#### Returns

-------
 - `Image.Image` - Flattened image

#### Signature

```python
def flattenAll(
    layers: list[Layer | Group] | list[Layer],
    imageDimensions: tuple[int, int],
    ignoreHidden: bool = True,
) -> Image.Image: ...
```



## flattenLayerOrGroup

[Show source in layeredimage.py:184](../../../layeredimage/layeredimage.py#L184)

Flatten a layer or group on to an image of what has already been flattened.

#### Arguments

----
 layerOrGroup (Layer, Group): A layer or a group of layers
 imageDimensions (tuple[int, int]): size of the image
 - `flattenedSoFar` *Image.Image, optional* - the image of what has already
 been flattened. Defaults to None.
 - `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
 to True.

#### Returns

-------
 - `Image.Image` - Flattened image

#### Signature

```python
def flattenLayerOrGroup(
    layerOrGroup: Layer | Group,
    imageDimensions: tuple[int, int],
    flattenedSoFar: Image.Image | None = None,
    ignoreHidden: bool = True,
) -> Image.Image: ...
```