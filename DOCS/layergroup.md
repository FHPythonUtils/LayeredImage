Module layeredimage.layergroup
==============================
Base class

Classes
-------

`Group(name, layers, dimensions=None, offsets=(0, 0), opacity=1.0, visible=True, blendmode=BlendType.NORMAL)`
:   A representation of an image group 
    
    A representation of an image group
    
    Args:
            name (string): Name of the layer or group
            layers (layeredimage.Layer[]): A list of layers where the next
            index stacks upon the previous layer
            dimensions ((int, int)): A tuple representing the dimensions in
            pixels
            offsets (tuple, optional): A tuple representing the left and top
            offsets in pixels. Defaults to (0, 0).
            opacity (float, optional): A float representing the alpha value
            where 0 is invisible and 1 is fully visible. Defaults to 1.0.
            visible (bool, optional): Is the layer visible to the user (this
            is often configured per layer or per group by an 'eye' icon).
            Defaults to True.

    ### Ancestors (in MRO)

    * layeredimage.layergroup.LayerGroup

    ### Methods

    `json(self)`
    :   Get the object as a dict

`Layer(name, image, dimensions=None, offsets=(0, 0), opacity=1.0, visible=True, blendmode=BlendType.NORMAL)`
:   A representation of an image layer 
    
    A representation of an image layer
    
    Args:
            name (string): Name of the layer or group
            image (PIL.Image): A PIL Image
            dimensions ((int, int)): A tuple representing the dimensions in
            pixels
            offsets (tuple, optional): A tuple representing the left and top
            offsets in pixels. Defaults to (0, 0).
            opacity (float, optional): A float representing the alpha value
            where 0 is invisible and 1 is fully visible. Defaults to 1.0.
            visible (bool, optional): Is the layer visible to the user (this
            is often configured per layer or per group by an 'eye' icon).
            Defaults to True.

    ### Ancestors (in MRO)

    * layeredimage.layergroup.LayerGroup

    ### Methods

    `json(self)`
    :   Get the object as a dict

`LayerGroup(name, dimensions, offsets=(0, 0), opacity=1.0, visible=True, layerGroup=LayerGroupTypes.LAYER, blendmode=BlendType.NORMAL, **kwargs)`
:   A representation of an image layer or group 
    
    A representation of an image layer or group
    
    Args:
            name (string): Name of the layer or group
            dimensions ((int, int)): A tuple representing the dimensions in
            pixels
            offsets (tuple, optional): A tuple representing the left and top
            offsets in pixels. Defaults to (0, 0).
            opacity (float, optional): A float representing the alpha value
            where 0 is invisible and 1 is fully visible. Defaults to 1.0.
            visible (bool, optional): Is the layer visible to the user (this
            is often configured per layer or per group by an 'eye' icon).
            Defaults to True.
            layerGroup ([type], optional): Type LAYER, GROUP, or UNDEFINED.
            Defaults to LayerGroupTypes.LAYER.

    ### Descendants

    * layeredimage.layergroup.Group
    * layeredimage.layergroup.Layer

`LayerGroupTypes(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   Can be a LAYER, GROUP, or UNDEFINED

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `GROUP`
    :

    `LAYER`
    :

    `UNDEFINED`
    :