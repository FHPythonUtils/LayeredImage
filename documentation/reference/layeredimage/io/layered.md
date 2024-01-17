# Layered

[Layeredimage Index](../../README.md#layeredimage-index) / [Layeredimage](../index.md#layeredimage) / [Io](./index.md#io) / Layered

> Auto-generated documentation for [layeredimage.io.layered](../../../../layeredimage/io/layered.py) module.

- [Layered](#layered)
  - [_saveLayer_LAYERED](#_savelayer_layered)
  - [grabLayer_LAYERED](#grablayer_layered)
  - [openLayer_LAYERED](#openlayer_layered)
  - [openLayer_LAYEREDC](#openlayer_layeredc)
  - [saveLayer_LAYERED](#savelayer_layered)
  - [saveLayer_LAYEREDC](#savelayer_layeredc)
  - [writeImage_LAYERED](#writeimage_layered)

## _saveLayer_LAYERED

[Show source in layered.py:101](../../../../layeredimage/io/layered.py#L101)

Save a layered image as .layered.

#### Signature

```python
def _saveLayer_LAYERED(
    fileName: str, layeredImage: LayeredImage, compressed: bool = False
) -> None: ...
```



## grabLayer_LAYERED

[Show source in layered.py:81](../../../../layeredimage/io/layered.py#L81)

Grab an image from .layered.

#### Signature

```python
def grabLayer_LAYERED(
    zipFile: ZipFile, layer: dict[str, Any], blendLookup: dict[str, Any]
): ...
```



## openLayer_LAYERED

[Show source in layered.py:19](../../../../layeredimage/io/layered.py#L19)

Open a .layered file into a layered image.

#### Signature

```python
def openLayer_LAYERED(file: str) -> LayeredImage: ...
```



## openLayer_LAYEREDC

[Show source in layered.py:131](../../../../layeredimage/io/layered.py#L131)

Open a .layeredc file into a layered image.

#### Signature

```python
def openLayer_LAYEREDC(file: str) -> LayeredImage: ...
```



## saveLayer_LAYERED

[Show source in layered.py:96](../../../../layeredimage/io/layered.py#L96)

Save a layered image as .layered.

#### Signature

```python
def saveLayer_LAYERED(fileName: str, layeredImage: LayeredImage) -> None: ...
```



## saveLayer_LAYEREDC

[Show source in layered.py:136](../../../../layeredimage/io/layered.py#L136)

Save a layeredc image as .layered.

#### Signature

```python
def saveLayer_LAYEREDC(fileName: str, layeredImage: LayeredImage) -> None: ...
```



## writeImage_LAYERED

[Show source in layered.py:119](../../../../layeredimage/io/layered.py#L119)

Write an image to the archive.

#### Signature

```python
def writeImage_LAYERED(
    image: Image.Image, zipFile: ZipFile, path: str, compressed: bool = False
): ...
```