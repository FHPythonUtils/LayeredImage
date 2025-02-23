import pytest
from PIL import Image

from layeredimage.layeredimage import LayeredImage
from layeredimage.layergroup import Group, Layer


@pytest.fixture
def example_layer():
	# Provide a simple example layer for testing
	return Layer(name="Example Layer", image=Image.new("RGBA", (100, 100)))


@pytest.fixture
def example_group(example_layer):
	# Provide a simple example group containing the example layer for testing
	return Group(name="Example Group", layers=[example_layer])


@pytest.fixture
def example_image(example_group):
	# Provide a simple example LayeredImage containing the example group for testing
	return LayeredImage(layersAndGroups=[example_group])


def test_layered_image_init() -> None:
	# Test initialization of LayeredImage
	img = LayeredImage([])
	assert isinstance(img, LayeredImage)


def test_add_layer_or_group(example_image, example_layer) -> None:
	# Test adding a layer to LayeredImage
	initial_count = len(example_image.layersAndGroups)
	example_image.addLayerOrGroup(example_layer)
	assert len(example_image.layersAndGroups) == initial_count + 1


def test_insert_layer_or_group(example_image, example_layer) -> None:
	# Test inserting a layer into LayeredImage
	example_image.insertLayerOrGroup(example_layer, 0)
	assert example_image.layersAndGroups[0] == example_layer


def test_remove_layer_or_group(example_image, example_layer) -> None:
	# Test removing a layer from LayeredImage
	example_image.addLayerOrGroup(example_layer)
	initial_count = len(example_image.layersAndGroups)
	example_image.removeLayerOrGroup(0)
	assert len(example_image.layersAndGroups) == initial_count - 1


def test_get_layer_or_group(example_image, example_group) -> None:
	# Test getting a layer or group from LayeredImage
	assert example_image.getLayerOrGroup(0) == example_group


def test_extract_layers(example_image, example_layer) -> None:
	# Test extracting layers from LayeredImage
	example_image.addLayerOrGroup(example_layer)
	assert len(example_image.extractLayers()) == 2


def test_update_layers(example_image, example_layer) -> None:
	# Test updating layers in LayeredImage
	example_image.addLayerOrGroup(example_layer)
	example_image.updateLayers()
	assert len(example_image.layers) == 2


def test_extract_groups(example_image, example_group) -> None:
	# Test extracting groups from LayeredImage
	assert len(example_image.extractGroups()) == 1


def test_update_groups(example_image, example_group) -> None:
	# Test updating groups in LayeredImage
	example_image.addLayerOrGroup(example_group)
	example_image.updateGroups()
	assert len(example_image.groups) == 2


def test_get_flatten_layers(example_image) -> None:
	# Test flattening layers in LayeredImage
	img = example_image.getFlattenLayers()
	assert isinstance(img, Image.Image)


def test_layered_image_repr(example_image) -> None:
	# Test string representation of LayeredImage
	assert repr(example_image) == str(example_image)


def test_layered_image_str(example_image) -> None:
	# Test string representation of LayeredImage
	assert str(example_image) == "<LayeredImage (100x100) with 1 children>"


def test_layered_image_json(example_image) -> None:
	# Test getting LayeredImage as a dictionary
	assert isinstance(example_image.json(), dict)
