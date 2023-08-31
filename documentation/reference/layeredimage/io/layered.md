# Layered

[Layeredimage Index](../../README.md#layeredimage-index) /
[Layeredimage](../index.md#layeredimage) /
[Io](./index.md#io) /
Layered

> Auto-generated documentation for [layeredimage.io.layered](../../../../layeredimage/io/layered.py) module.

- [Layered](#layered)
  - [grabLayer_LAYERED](#grablayer_layered)
  - [openLayer_LAYERED](#openlayer_layered)
  - [openLayer_LAYEREDC](#openlayer_layeredc)
  - [saveLayer_LAYERED](#savelayer_layered)
  - [saveLayer_LAYEREDC](#savelayer_layeredc)
  - [writeImage_LAYERED](#writeimage_layered)

## grabLayer_LAYERED

[Show source in layered.py:83](../../../../layeredimage/io/layered.py#L83)

Grab an image from .layered.

#### Signature

```python
def grabLayer_LAYERED(
    zipFile: ZipFile, layer: dict[str, Any], blendLookup: dict[str, Any]
):
    ...
```



## openLayer_LAYERED

[Show source in layered.py:21](../../../../layeredimage/io/layered.py#L21)

Open a .layered file into a layered image.

#### Signature

```python
def openLayer_LAYERED(file: str) -> LayeredImage:
    ...
```



## openLayer_LAYEREDC

[Show source in layered.py:133](../../../../layeredimage/io/layered.py#L133)

Open a .layeredc file into a layered image.

#### Signature

```python
def openLayer_LAYEREDC(file: str) -> LayeredImage:
    ...
```



## saveLayer_LAYERED

[Show source in layered.py:98](../../../../layeredimage/io/layered.py#L98)

Save a layered image as .layered.

#### Signature

```python
def saveLayer_LAYERED(fileName: str, layeredImage: LayeredImage) -> None:
    ...
```



## saveLayer_LAYEREDC

[Show source in layered.py:138](../../../../layeredimage/io/layered.py#L138)

Save a layeredc image as .layered.

#### Signature

```python
def saveLayer_LAYEREDC(fileName: str, layeredImage: LayeredImage) -> None:
    ...
```



## writeImage_LAYERED

[Show source in layered.py:121](../../../../layeredimage/io/layered.py#L121)

Write an image to the archive.

#### Signature

```python
def writeImage_LAYERED(
    image: Image.Image, zipFile: ZipFile, path: str, compressed: bool = False
):
    ...
```