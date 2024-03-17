# LayeredImage

[Layeredimage Index](../README.md#layeredimage-index) / [Layeredimage](./index.md#layeredimage) / LayeredImage

> Auto-generated documentation for [layeredimage.layeredimage](../../../layeredimage/layeredimage.py) module.

- [LayeredImage](#layeredimage)
  - [LayeredImage](#layeredimage-1)
    - [LayeredImage().__repr__](#layeredimage()__repr__)
    - [LayeredImage().__str__](#layeredimage()__str__)
    - [LayeredImage().addLayerOrGroup](#layeredimage()addlayerorgroup)
    - [LayeredImage().extractGroups](#layeredimage()extractgroups)
    - [LayeredImage().extractLayers](#layeredimage()extractlayers)
    - [LayeredImage().getFlattenLayers](#layeredimage()getflattenlayers)
    - [LayeredImage().getLayerOrGroup](#layeredimage()getlayerorgroup)
    - [LayeredImage().insertLayerOrGroup](#layeredimage()insertlayerorgroup)
    - [LayeredImage().json](#layeredimage()json)
    - [LayeredImage().removeLayerOrGroup](#layeredimage()removelayerorgroup)
    - [LayeredImage().updateGroups](#layeredimage()updategroups)
    - [LayeredImage().updateLayers](#layeredimage()updatelayers)
  - [render](#render)

## LayeredImage

[Show source in layeredimage.py:14](../../../layeredimage/layeredimage.py#L14)

A representation of a layered image such as an ora.

#### Signature

```python
class LayeredImage:
    def __init__(
        self,
        layersAndGroups: list[Layer | Group],
        dimensions: tuple[int, int] | None = None,
        **kwargs: dict[str, Any]
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

### LayeredImage().addLayerOrGroup

[Show source in layeredimage.py:69](../../../layeredimage/layeredimage.py#L69)

Add a LayerOrGroup.

#### Signature

```python
def addLayerOrGroup(self, layerOrGroup: Layer | Group) -> None: ...
```

### LayeredImage().extractGroups

[Show source in layeredimage.py:125](../../../layeredimage/layeredimage.py#L125)

Extract the groups from the image.

#### Signature

```python
def extractGroups(self) -> list[Group]: ...
```

#### See also

- [Group](./layergroup.md#group)

### LayeredImage().extractLayers

[Show source in layeredimage.py:94](../../../layeredimage/layeredimage.py#L94)

Extract the layers from the image.

#### Signature

```python
def extractLayers(self) -> list[Layer]: ...
```

#### See also

- [Layer](./layergroup.md#layer)

### LayeredImage().getFlattenLayers

[Show source in layeredimage.py:82](../../../layeredimage/layeredimage.py#L82)

Return an image for all flattened layers.

#### Signature

```python
def getFlattenLayers(self) -> Image.Image: ...
```

### LayeredImage().getLayerOrGroup

[Show source in layeredimage.py:65](../../../layeredimage/layeredimage.py#L65)

Get a LayerOrGroup.

#### Signature

```python
def getLayerOrGroup(self, index: int) -> Layer | Group: ...
```

### LayeredImage().insertLayerOrGroup

[Show source in layeredimage.py:73](../../../layeredimage/layeredimage.py#L73)

Insert a LayerOrGroup at a specific index.

#### Signature

```python
def insertLayerOrGroup(self, layerOrGroup: Layer | Group, index: int) -> None: ...
```

### LayeredImage().json

[Show source in layeredimage.py:59](../../../layeredimage/layeredimage.py#L59)

Get the object as a dict.

#### Signature

```python
def json(self) -> dict[str, Any]: ...
```

### LayeredImage().removeLayerOrGroup

[Show source in layeredimage.py:77](../../../layeredimage/layeredimage.py#L77)

Remove a LayerOrGroup at a specific index.

#### Signature

```python
def removeLayerOrGroup(self, index: int) -> None: ...
```

### LayeredImage().updateGroups

[Show source in layeredimage.py:133](../../../layeredimage/layeredimage.py#L133)

Update the groups from the image.

#### Signature

```python
def updateGroups(self) -> None: ...
```

### LayeredImage().updateLayers

[Show source in layeredimage.py:121](../../../layeredimage/layeredimage.py#L121)

Update the layers from the image.

#### Signature

```python
def updateLayers(self) -> None: ...
```



## render

[Show source in layeredimage.py:138](../../../layeredimage/layeredimage.py#L138)

Flatten a layer or group on to an image of what has already been flattened.

#### Arguments

----
 layerOrGroup (Layer, Group): A layer or a group of layers
 - `project_image` *np.ndarray, optional* - the image of what has already
 been flattened.

#### Returns

-------
 - `np.ndarray` - Flattened image

#### Signature

```python
def render(layerOrGroup: Layer | Group, project_image: np.ndarray) -> np.ndarray: ...
```