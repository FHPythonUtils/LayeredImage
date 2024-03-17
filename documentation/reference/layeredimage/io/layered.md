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

[Show source in layered.py:105](../../../../layeredimage/io/layered.py#L105)

Save a layered image as .layered.

#### Signature

```python
def _saveLayer_LAYERED(
    fileName: str, layeredImage: LayeredImage, compressed: bool = False
) -> None: ...
```

#### See also

- [LayeredImage](../layeredimage.md#layeredimage)



## grabLayer_LAYERED

[Show source in layered.py:83](../../../../layeredimage/io/layered.py#L83)

Grab an image from .layered.

#### Signature

```python
def grabLayer_LAYERED(
    zipFile: ZipFile, layer: dict[str, Any], blendLookup: dict[str, Any]
) -> Layer: ...
```

#### See also

- [Layer](../layergroup.md#layer)



## openLayer_LAYERED

[Show source in layered.py:21](../../../../layeredimage/io/layered.py#L21)

Open a .layered file into a layered image.

#### Signature

```python
def openLayer_LAYERED(file: str) -> LayeredImage: ...
```

#### See also

- [LayeredImage](../layeredimage.md#layeredimage)



## openLayer_LAYEREDC

[Show source in layered.py:142](../../../../layeredimage/io/layered.py#L142)

Open a .layeredc file into a layered image.

#### Signature

```python
def openLayer_LAYEREDC(file: str) -> LayeredImage: ...
```

#### See also

- [LayeredImage](../layeredimage.md#layeredimage)



## saveLayer_LAYERED

[Show source in layered.py:100](../../../../layeredimage/io/layered.py#L100)

Save a layered image as .layered.

#### Signature

```python
def saveLayer_LAYERED(fileName: str, layeredImage: LayeredImage) -> None: ...
```

#### See also

- [LayeredImage](../layeredimage.md#layeredimage)



## saveLayer_LAYEREDC

[Show source in layered.py:147](../../../../layeredimage/io/layered.py#L147)

Save a layeredc image as .layered.

#### Signature

```python
def saveLayer_LAYEREDC(fileName: str, layeredImage: LayeredImage) -> None: ...
```

#### See also

- [LayeredImage](../layeredimage.md#layeredimage)



## writeImage_LAYERED

[Show source in layered.py:127](../../../../layeredimage/io/layered.py#L127)

Write an image to the archive.

#### Signature

```python
def writeImage_LAYERED(
    image: Image.Image, zipFile: ZipFile, path: str, compressed: bool = False
) -> None: ...
```