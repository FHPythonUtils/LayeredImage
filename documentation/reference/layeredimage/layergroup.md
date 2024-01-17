# LayerGroup

[Layeredimage Index](../README.md#layeredimage-index) / [Layeredimage](./index.md#layeredimage) / LayerGroup

> Auto-generated documentation for [layeredimage.layergroup](../../../layeredimage/layergroup.py) module.

- [LayerGroup](#layergroup)
  - [Group](#group)
    - [Group().json](#group()json)
  - [Layer](#layer)
    - [Layer().json](#layer()json)
  - [LayerGroup](#layergroup-1)
    - [LayerGroup().__repr__](#layergroup()__repr__)
    - [LayerGroup().__str__](#layergroup()__str__)
    - [LayerGroup().json](#layergroup()json)

## Group

[Show source in layergroup.py:128](../../../layeredimage/layergroup.py#L128)

A representation of an image group.

#### Signature

```python
class Group(LayerGroup):
    def __init__(
        self,
        name: str,
        layers: list[Layer],
        dimensions: tuple[int, int] | None = None,
        offsets: tuple[int, int] = (0, 0),
        opacity: float = 1.0,
        visible: bool = True,
        blendmode: BlendType = BlendType.NORMAL,
    ): ...
```

#### See also

- [LayerGroup](#layergroup)
- [Layer](#layer)

### Group().json

[Show source in layergroup.py:175](../../../layeredimage/layergroup.py#L175)

Get the object as a dict.

#### Signature

```python
def json(self) -> dict[str, Any]: ...
```



## Layer

[Show source in layergroup.py:77](../../../layeredimage/layergroup.py#L77)

A representation of an image layer.

#### Signature

```python
class Layer(LayerGroup):
    def __init__(
        self,
        name: str,
        image: Image.Image,
        dimensions: tuple[int, int] | None = None,
        offsets: tuple[int, int] = (0, 0),
        opacity: float = 1.0,
        visible: bool = True,
        blendmode: BlendType = BlendType.NORMAL,
    ): ...
```

#### See also

- [LayerGroup](#layergroup)

### Layer().json

[Show source in layergroup.py:115](../../../layeredimage/layergroup.py#L115)

Get the object as a dict.

#### Signature

```python
def json(self) -> dict[str, Any]: ...
```



## LayerGroup

[Show source in layergroup.py:11](../../../layeredimage/layergroup.py#L11)

A representation of an image layer or group.

#### Signature

```python
class LayerGroup:
    def __init__(
        self,
        name: str,
        dimensions: tuple[int, int],
        offsets: tuple[int, int] = (0, 0),
        opacity: float = 1.0,
        visible: bool = True,
        blendmode: BlendType = BlendType.NORMAL,
        **kwargs: Any
    ): ...
```

### LayerGroup().__repr__

[Show source in layergroup.py:48](../../../layeredimage/layergroup.py#L48)

Get the string representation.

#### Signature

```python
def __repr__(self): ...
```

### LayerGroup().__str__

[Show source in layergroup.py:52](../../../layeredimage/layergroup.py#L52)

Get the string representation.

#### Signature

```python
def __str__(self): ...
```

### LayerGroup().json

[Show source in layergroup.py:65](../../../layeredimage/layergroup.py#L65)

Get the object as a dict.

#### Signature

```python
def json(self) -> dict[str, Any]: ...
```