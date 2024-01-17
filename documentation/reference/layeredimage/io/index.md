# Io

[Layeredimage Index](../../README.md#layeredimage-index) / [Layeredimage](../index.md#layeredimage) / Io

> Auto-generated documentation for [layeredimage.io](../../../../layeredimage/io/__init__.py) module.

- [Io](#io)
  - [exportFlatImage](#exportflatimage)
  - [extNotRecognised](#extnotrecognised)
  - [openLayerImage](#openlayerimage)
  - [saveLayerImage](#savelayerimage)
  - [Modules](#modules)

## exportFlatImage

[Show source in __init__.py:109](../../../../layeredimage/io/__init__.py#L109)

Export the layered image to a unilayer image file.

#### Signature

```python
def exportFlatImage(fileName: str, layeredImage: LayeredImage) -> None: ...
```



## extNotRecognised

[Show source in __init__.py:24](../../../../layeredimage/io/__init__.py#L24)

Output the file extension not recognised error.

#### Signature

```python
def extNotRecognised(fileName: str): ...
```



## openLayerImage

[Show source in __init__.py:34](../../../../layeredimage/io/__init__.py#L34)

Open a layer image file into a layer image object.

#### Arguments

----
 - `file` *str* - path/ filename

#### Raises

------
 - `FileExistsError` - If the layered image does not exist
 - `ValueError` - If the extention is not recognised

#### Returns

-------
 - `LayeredImage` - a layered image object

#### Signature

```python
def openLayerImage(file: str | Path) -> LayeredImage: ...
```



## saveLayerImage

[Show source in __init__.py:73](../../../../layeredimage/io/__init__.py#L73)

Save a layered image to a file.

#### Arguments

----
 - `fileName` *str* - path/ filename
 - `layeredImage` *LayeredImage* - the layered image to save

#### Raises

------
 - `ValueError` - If the extention is not recognised

#### Returns

-------
 None

#### Signature

```python
def saveLayerImage(fileName: str | Path, layeredImage: LayeredImage) -> None: ...
```



## Modules

- [Common](./common.md)
- [Gif](./gif.md)
- [Layered](./layered.md)
- [Lsr](./lsr.md)
- [Ora](./ora.md)
- [Pdn](./pdn.md)
- [Psd](./psd.md)
- [Tiff](./tiff.md)
- [Webp](./webp.md)
- [Xcf](./xcf.md)