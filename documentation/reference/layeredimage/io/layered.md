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

[Show source in layered.py:104](../../../../layeredimage/io/layered.py#L104)

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

[Show source in layered.py:82](../../../../layeredimage/io/layered.py#L82)

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

[Show source in layered.py:20](../../../../layeredimage/io/layered.py#L20)

Open a .layered file into a layered image.

#### Signature

```python
def openLayer_LAYERED(file: str) -> LayeredImage: ...
```

#### See also

- [LayeredImage](../layeredimage.md#layeredimage)



## openLayer_LAYEREDC

[Show source in layered.py:141](../../../../layeredimage/io/layered.py#L141)

Open a .layeredc file into a layered image.

#### Signature

```python
def openLayer_LAYEREDC(file: str) -> LayeredImage: ...
```

#### See also

- [LayeredImage](../layeredimage.md#layeredimage)



## saveLayer_LAYERED

[Show source in layered.py:99](../../../../layeredimage/io/layered.py#L99)

Save a layered image as .layered.

#### Signature

```python
def saveLayer_LAYERED(fileName: str, layeredImage: LayeredImage) -> None: ...
```

#### See also

- [LayeredImage](../layeredimage.md#layeredimage)



## saveLayer_LAYEREDC

[Show source in layered.py:146](../../../../layeredimage/io/layered.py#L146)

Save a layeredc image as .layered.

#### Signature

```python
def saveLayer_LAYEREDC(fileName: str, layeredImage: LayeredImage) -> None: ...
```

#### See also

- [LayeredImage](../layeredimage.md#layeredimage)



## writeImage_LAYERED

[Show source in layered.py:126](../../../../layeredimage/io/layered.py#L126)

Write an image to the archive.

#### Signature

```python
def writeImage_LAYERED(
    image: Image.Image, zipFile: ZipFile, path: str, compressed: bool = False
) -> None: ...
```