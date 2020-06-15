Module layeredimage.layeredimage
================================
LayeredImage class

Functions
---------

    
`flattenAll(layers, imageDimensions, ignoreHidden)`
:   Flatten a list of layers and groups
    
    Args:
            layers ([Layer|Group]): A list of layers and groups
            imageDimensions ((int, int)): size of the image
            been flattened. Defaults to None.
            ignoreHidden (bool, optional): ignore layers that are hidden. Defaults
            to True.
    
    Returns:
            PIL.Image: Flattened image

    
`flattenLayerOrGroup(layerOrGroup, imageDimensions, flattenedSoFar=None, ignoreHidden=True)`
:   Flatten a layer or group on to an image of what has already been
    flattened
    
    Args:
            layerOrGroup (Layer|Group): A layer or a group of layers
            imageDimensions ((int, int)): size of the image
            flattenedSoFar (PIL.Image, optional): the image of what has already
            been flattened. Defaults to None.
            ignoreHidden (bool, optional): ignore layers that are hidden. Defaults
            to True.
    
    Returns:
            PIL.Image: Flattened image

    
`rasterImageOA(image, size, alpha=1.0, offsets=(0, 0))`
:   Rasterise an image with offset and alpha to a given size

    
`rasterImageOffset(image, size, offsets=(0, 0))`
:   Rasterise an image with offset to a given size

Classes
-------

`LayeredImage(layersAndGroups, dimensions=None, **kwargs)`
:   A representation of a layered image such as an ora

    ### Methods

    `addLayerOrGroup(self, LayerOrGroup)`
    :   Add a LayerOrGroup

    `addLayerRaster(self, image, name)`
    :   Raster an image and add as a layer

    `extractGroups(self)`
    :   Extract the groups from the image

    `extractLayers(self)`
    :   Extract the layers from the image

    `flattenLayers(self, ignoreHidden=True)`
    :   Flatten all layers

    `flattenTwoLayers(self, background, foreground, ignoreHidden=True)`
    :   Flatten two layers

    `getFlattenLayers(self, ignoreHidden=True)`
    :   Return an image for all flattened layers

    `getFlattenTwoLayers(self, background, foreground, ignoreHidden=True)`
    :   Return an image for two flattened layers

    `getLayerOrGroup(self, index)`
    :   Get a LayerOrGroup

    `insertLayerOrGroup(self, LayerOrGroup, index)`
    :   Insert a LayerOrGroup at a specific index

    `insertLayerRaster(self, image, name, index)`
    :   Raster an image and insert the layer

    `json(self)`
    :   Get the object as a dict

    `removeLayerOrGroup(self, index)`
    :   Remove a LayerOrGroup at a specific index

    `updateGroups(self)`
    :   Update the groups from the image

    `updateLayers(self)`
    :   Update the layers from the image