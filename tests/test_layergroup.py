import pytest
from PIL import Image

from layeredimage.layergroup import Group, Layer


@pytest.fixture()
def example_image():
    # Provide a simple example PIL image for testing
    return Image.new("RGBA", (100, 100))

@pytest.fixture()
def example_layer(example_image):
    # Provide a simple example layer for testing
    return Layer(name="Example Layer", image=example_image)

@pytest.fixture()
def example_group(example_layer):
    # Provide a simple example group containing the example layer for testing
    return Group(name="Example Group", layers=[example_layer])

def test_layer_group_init(example_image) -> None:
    # Test initialization of LayerGroup
    layer_group = Layer(name="Test Layer", dimensions=(100, 100), image=example_image)
    assert isinstance(layer_group, Layer)

def test_layer_init(example_image) -> None:
    # Test initialization of Layer
    layer = Layer(name="Test Layer", image=example_image)
    assert isinstance(layer, Layer)

def test_group_init(example_layer) -> None:
    # Test initialization of Group
    group = Group(name="Test Group", layers=[example_layer])
    assert isinstance(group, Group)

def test_layer_group_repr(example_layer) -> None:
    # Test string representation of LayerGroup
    assert repr(example_layer) == str(example_layer)

def test_layer_group_str(example_layer) -> None:
    # Test string representation of LayerGroup
    assert str(example_layer) == f'<LayeredImage "{example_layer.name}" ({example_layer.dimensions[0]}x{example_layer.dimensions[1]})>'

def test_layer_json(example_layer) -> None:
    # Test getting Layer as a dictionary
    assert isinstance(example_layer.json(), dict)

def test_group_json(example_group) -> None:
    # Test getting Group as a dictionary
    assert isinstance(example_group.json(), dict)
