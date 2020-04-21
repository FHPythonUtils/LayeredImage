""" Do file io """

# To avoid throwing import errors for the sake of it, specialised imports are
# to be scoped to the function
# pylint: disable=import-outside-toplevel

from os.path import exists
from sys import exit as sysexit
from metprint import LogType, Logger, FHFormatter
from layeredimage.layergroup import LayerGroupTypes, Layer, Group
from layeredimage.layeredimage import LayeredImage, rasterImageOA

def openLayerImage(file):
	"""Open a layer image file into a layer image object

	Args:
		file (string): path/ filename

	Returns:
		LayeredImage: a layered image object
	"""
	checkExists(file)
	if file[-3:] == "ora":
		return openLayer_ORA(file)
	if file[-3:] == "psd":
		return openLayer_PSD(file)
	if file[-3:] == "xcf":
		return openLayer_XCF(file)
	if file[-3:] == "pdn":
		return openLayer_PDN(file)
	return LayeredImage([], (0, 0))

def saveLayerImage(fileName, layeredImage):
	"""Save a layered image to a file

	Args:
		fileName (string): path/ filename
		layeredImage (LayeredImage): the layered image to save
	"""
	if fileName[-3:] == "ora":
		saveLayer_ORA(fileName, layeredImage)
	if fileName[-3:] == "psd":
		saveLayer_PSD(fileName, layeredImage)
	if fileName[-3:] == "xcf":
		saveLayer_XCF(fileName, layeredImage)
	if fileName[-3:] == "pdn":
		saveLayer_PDN(fileName, layeredImage)

def checkExists(file):
	""" Throw an error and abort if the path does not exist """
	if not exists(file):
		Logger(FHFormatter()).logPrint(file + " does not exist", LogType.ERROR)
		sysexit(1)

#### ORA ####

def openLayer_ORA(file):
	""" Open an .ora file into a layered image """
	from pyora import Project, TYPE_LAYER
	layersAndGroups = []
	project = Project.load(file)
	for layerOrGroup in project.children[::-1]:
		if layerOrGroup.type == TYPE_LAYER:
			layersAndGroups.append(Layer(layerOrGroup.name, layerOrGroup.get_image_data(True),
			layerOrGroup.dimensions, layerOrGroup.offsets, layerOrGroup.opacity, layerOrGroup.visible))
		else:
			layers = []
			for layer in list(layerOrGroup.children)[::-1]:
				layers.append(Layer(layer.name, layer.get_image_data(True), layer.dimensions, layer.offsets,
				layer.opacity, layer.visible))
			layersAndGroups.append(Group(layerOrGroup.name, layers, project.dimensions, layerOrGroup.offsets,
			layerOrGroup.opacity, layerOrGroup.visible))
	return LayeredImage(layersAndGroups, project.dimensions)

def saveLayer_ORA(fileName, layeredImage):
	""" Save a layered image as .ora """
	from pyora import Project
	project = Project.new(layeredImage.dimensions[0], layeredImage.dimensions[1])
	for layerOrGroup in layeredImage.layersAndGroups:
		if layerOrGroup.type == LayerGroupTypes.LAYER:
			project = addLayer_ORA(project, layerOrGroup)
		else:
			for layer in layerOrGroup.layers:
				project = addLayer_ORA(project, layer, layerOrGroup.name + "/")
	Project.save = save_ORA_fix
	project.save(fileName)

def addLayer_ORA(project, layer, groupName=""):
	""" Update the project with a shiny new layer """
	project.add_layer(layer.image,
	groupName + layer.name,
	offsets=(int(layer.offsets[0] / 2), int(layer.offsets[1] / 2)),
	opacity=layer.opacity,
	visible=layer.visible)
	return project

def save_ORA_fix(self, path_or_file, composite_image=None, use_original=False):
	""" Patch the Project.save function from pyora 3.0 with a newer version -Future
	This snippet is MIT License Copyright (c) 2019 Paul Jewell
	"""
	# This is a patch, so im going to need to access what I please
	# pylint: disable=protected-access
	import zipfile
	from defusedxml import ElementTree as ET
	from pyora.Render import Renderer, make_thumbnail
	from pyora import TYPE_LAYER
	with zipfile.ZipFile(path_or_file, 'w') as zipref:
		zipref.writestr('mimetype', "image/openraster".encode())
		zipref.writestr('stack.xml', ET.tostring(self._elem_root, method='xml'))
		if not composite_image:
			if use_original and self._extracted_merged_image:
				composite_image = self._extracted_merged_image
			else:
				# render using our built in library
				r = Renderer(self)
				composite_image = r.render()
		self._zip_store_image(zipref, 'mergedimage.png', composite_image)
		make_thumbnail(composite_image)  # works in place
		self._zip_store_image(zipref, 'Thumbnails/thumbnail.png', composite_image)

		for layer in self.children_recursive:
			if layer.type == TYPE_LAYER:
				self._zip_store_image(zipref, layer['src'], layer.get_image_data())
	# pylint: enable=protected-access


#### PSD ####
def openLayer_PSD(file):
	""" Open an .psd file into a layered image """
	from psd_tools import PSDImage
	layersAndGroups = []
	project = PSDImage.load(file)
	for layerOrGroup in project.layers[::-1]:
		if layerOrGroup.is_group():
			layers = []
			for layer in layerOrGroup.layers:
				layers.append(Layer(layer.name, layer.as_PIL(), (layer.width,
				layer.height), (layer.left, layer.top),
				layer.opacity / 255, layer.visible))
			layersAndGroups.append(Group(layerOrGroup.name, layers, (layerOrGroup.width,
			layerOrGroup.height), (layerOrGroup.left, layerOrGroup.top),
			layerOrGroup.opacity / 255, layerOrGroup.visible))
		else:
			layersAndGroups.append(
			Layer(layerOrGroup.name, layerOrGroup.as_PIL(), (layerOrGroup.width,
			layerOrGroup.height), (layerOrGroup.left, layerOrGroup.top),
			layerOrGroup.opacity / 255, layerOrGroup.visible))
	return LayeredImage(layersAndGroups, (project.width, project.height))


def saveLayer_PSD(_fileName, _layeredImage):
	""" Save a layered image as .psd """
	Logger(FHFormatter()).logPrint("Saving PSDs is not implemented in psd-tools3 - " +
	"this is present in psd-tools, however, installing it on Windows is difficult so " +
	"I am not currently using this library", LogType.ERROR)
	raise NotImplementedError


#### XCF ####

def openLayer_XCF(file):
	""" Open an .xcf file into a layered image """
	from gimpformats_unofficial.gimpXcfDocument import GimpDocument
	project = GimpDocument(file)
	# Iterate the layers and create a list of layers for each group, then remove
	# these from the project layers
	layers = project.layers[::-1]
	index = 0
	groupIndex = 0
	groupLayers = [[]]
	while index < len(layers):
		layerOrGroup = layers[index]
		if layerOrGroup.isGroup:
			index -= 1
			while layers[index].itemPath is not None:
				layer = layers[index]
				groupLayers[groupIndex].append(Layer(layer.name, layer.image,
				(layer.width, layer.height), (layer.xOffset, layer.yOffset),
				layer.opacity, layer.visible))
				layers.pop(index)
				index -= 1
			index += 2
			groupIndex += 1
			groupLayers.append([])
		else:
			index += 1
	# Iterate the clean project layers and add the group layers in
	groupIndex = 0
	layersAndGroups = []
	for layerOrGroup in layers:
		if layerOrGroup.isGroup:
			layersAndGroups.append(Group(layerOrGroup.name, groupLayers[groupIndex][::-1],
				(layerOrGroup.width, layerOrGroup.height), (layerOrGroup.xOffset,
				layerOrGroup.yOffset), layerOrGroup.opacity, layerOrGroup.visible))
			groupIndex += 1
		else:
			layersAndGroups.append(Layer(layerOrGroup.name, layerOrGroup.image,
				(layerOrGroup.width, layerOrGroup.height), (layerOrGroup.xOffset,
				layerOrGroup.yOffset), layerOrGroup.opacity, layerOrGroup.visible))

	return LayeredImage(layersAndGroups, (project.width, project.height))




def saveLayer_XCF(fileName, layeredImage):
	""" Save a layered image as .xcf """
	Logger(FHFormatter()).logPrint("Saving XCFs is not implemented in gimpformats - " +
	"this is a little misleading as functions are pressent, however these are not " +
	"functional", LogType.ERROR)
	raise NotImplementedError


#### PDN ####
def openLayer_PDN(file):
	""" Open an .pdn file into a layered image """
	from pypdn import read
	from pypdn.namedlist import _make_fn
	from PIL import Image
	_make_fn = makeFn_PDN_fix
	project = read(file)
	layers = []
	for layer in project.layers:
		image = Image.fromarray(layer.image)
		layers.append(Layer(layer.name, image, image.size, (0, 0),
		layer.opacity / 255, layer.visible))
	return LayeredImage(layers, (project.width, project.height))

def saveLayer_PDN(_fileName, _layeredImage):
	""" Save a layered image as .pdn """
	Logger(FHFormatter()).logPrint("Saving PDNs is not implemented in pypdn", LogType.ERROR)
	raise NotImplementedError


def makeFn_PDN_fix(name, chain_fn, args, defaults):
	"""Patch the function pypdn.namedlist._make_fn with a python 3.8 compatible
	version
	This snippet is MIT License Copyright (c) 2018 Addison Elliott
	"""
	import ast
	import sys
	args_with_self = ['_self'] + list(args)
	arguments = [ast.Name(id=arg, ctx=ast.Load()) for arg in args_with_self]
	defs = [ast.Name(id='_def{0}'.format(idx), ctx=ast.Load()) for idx, _ in enumerate(defaults)]
	# Python 3.8 version
	if sys.version_info[0] >= 3 and sys.version_info >= 8:
		parameters = ast.arguments(args=[ast.arg(arg=arg) for arg in args_with_self],
		posonlyargs=[],	kwonlyargs=[], defaults=defs, kw_defaults=[])
		module_node = ast.Module(body=[ast.FunctionDef(
			name=name, args=parameters, body=[ast.Return(
				value=ast.Call(
					func=ast.Name(
						id='_chain', ctx=ast.Load()),
					args=arguments, keywords=[])
				)],
			decorator_list=[])], type_ignores=[])
	else:
		# Python 3 version
		parameters = ast.arguments(args=[ast.arg(arg=arg) for arg in args_with_self],
			kwonlyargs=[], defaults=defs, kw_defaults=[])
		module_node = ast.Module(body=[ast.FunctionDef(
			name=name, args=parameters, body=[ast.Return(
				value=ast.Call(
					func=ast.Name(
						id='_chain', ctx=ast.Load()),
					args=arguments, keywords=[])
				)],
			decorator_list=[])])
	module_node = ast.fix_missing_locations(module_node)
	# compile the ast
	code = compile(module_node, '<string>', 'exec')
	# and eval it in the right context
	globals_ = {'_chain': chain_fn}
	locals_ = dict(('_def{0}'.format(idx), value) for idx, value in enumerate(defaults))
	# locals_['_def0'] = []
	eval(code, globals_, locals_)
	# extract our function from the newly created module
	return locals_[name]
