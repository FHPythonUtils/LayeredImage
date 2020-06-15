Module layeredimage.io
======================
Do file io

Functions
---------

    
`addElem_fix(self, tag, parent_elem, name, z_index=1, offsets=(0, 0), opacity=1.0, visible=True, composite_op='svg:src-over', **kwargs)`
:   Patch the Project.save function from pyora 3.0 with a newer version -Future
    This snippet is MIT License Copyright (c) 2019 Paul Jewell

    
`addLayer_ORA(project, layer, blendLookup)`
:   Update the project with a shiny new layer

    
`blendModeLookup(blendmode, blendLookup, default=BlendType.NORMAL)`
:   Get the blendmode from a lookup table

    
`exportFlatImage(fileName, layeredImage)`
:   Export the layered image to a unilayer image file

    
`extNotRecognised(fileName)`
:   Output the file extension not recognised error

    
`getRasterLayers(layeredImage, imageFormat)`
:   Return layers and throw a warning if the image has groups

    
`grabLayer_LAYERED(zipFile, layer, blendLookup)`
:   Grab an image from .layered

    
`openLayerImage(file)`
:   Open a layer image file into a layer image object
    
    Args:
            file (string): path/ filename
    
    Returns:
            LayeredImage: a layered image object

    
`openLayer_GIF(file)`
:   Open a .gif file into a layered image

    
`openLayer_LAYERED(file)`
:   Open a .layered file into a layered image

    
`openLayer_LAYEREDC(file)`
:   Open a .layeredc file into a layered image

    
`openLayer_LSR(file)`
:   Open a .lsr file into a layered image

    
`openLayer_ORA(file)`
:   Open an .ora file into a layered image

    
`openLayer_PDN(file)`
:   Open a .pdn file into a layered image

    
`openLayer_PSD(file)`
:   Open a .psd file into a layered image

    
`openLayer_TIFF(file)`
:   Open a .tiff or a .tif file into a layered image

    
`openLayer_WEBP(file)`
:   Open a .webp file into a layered image

    
`openLayer_XCF(file)`
:   Open an .xcf file into a layered image

    
`saveLayerImage(fileName, layeredImage)`
:   Save a layered image to a file
    
    Args:
            fileName (string): path/ filename
            layeredImage (LayeredImage): the layered image to save

    
`saveLayer_GIF(fileName, layeredImage)`
:   Save a layered image as .gif

    
`saveLayer_LAYERED(fileName, layeredImage, compressed=False)`
:   Save a layered image as .layered

    
`saveLayer_LAYEREDC(fileName, layeredImage)`
:   Save a layeredc image as .layered

    
`saveLayer_LSR(fileName, layeredImage)`
:   Save a layered image as .lsr

    
`saveLayer_ORA(fileName, layeredImage)`
:   Save a layered image as .ora

    
`saveLayer_PDN(_fileName, _layeredImage)`
:   Save a layered image as .pdn

    
`saveLayer_PSD(_fileName, _layeredImage)`
:   Save a layered image as .psd

    
`saveLayer_TIFF(fileName, layeredImage)`
:   Save a layered image as .tiff or .tif

    
`saveLayer_WEBP(fileName, layeredImage)`
:   Save a layered image as .webp

    
`saveLayer_XCF(_fileName, _layeredImage)`
:   Save a layered image as .xcf

    
`writeImage_LAYERED(image, zipFile, path, compressed=False)`
:   Write an image to the archive