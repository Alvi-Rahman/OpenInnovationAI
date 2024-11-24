"""
File for Testing the Colormap
Created on Sun Nov 24
Author @TakrimRahmanAlbi
"""
import pytest
import numpy as np

from utils.colormap import get_normalized_pixels, apply_colormap


# Test get_normalized_pixels function
def test_get_normalized_pixels():
    # Test with a simple list of pixel values
    pixels = [0, 127, 255]
    normalized_pixels = get_normalized_pixels(pixels)

    # Expected normalized values (should be in the range 0.0 to 1.0)
    expected_normalized = [0.0, 0.498, 1.0]  # Normalize values between 0 and 255

    # Check if the result is close to the expected normalized values (with a small tolerance)
    assert np.allclose(normalized_pixels, expected_normalized, atol=0.001)


def test_get_normalized_pixels_empty():
    # Test with an empty list
    pixels = []
    normalized_pixels = get_normalized_pixels(pixels)

    # The result should be an empty array
    assert len(normalized_pixels) == 0


# Test apply_colormap function
def test_apply_colormap_default():
    pixels = [0, 127, 255]
    colormap_name = "viridis"  # Default colormap

    colored_pixels = apply_colormap(pixels, colormap_name)

    # Check that the returned colored pixels are in the form of RGB tuples
    assert len(colored_pixels) == len(pixels)
    assert len(colored_pixels[0]) == 3  # Should be in (R, G, B) format

    # Check that the values are within the valid RGB range [0, 255]
    for pixel in colored_pixels:
        assert all(0 <= channel <= 255 for channel in pixel)


def test_apply_colormap_custom():
    pixels = [0, 127, 255]
    colormap_name = "plasma"  # Use a custom colormap

    colored_pixels = apply_colormap(pixels, colormap_name)

    # Check that the returned colored pixels are in the form of RGB tuples
    assert len(colored_pixels) == len(pixels)
    assert len(colored_pixels[0]) == 3  # Should be in (R, G, B) format

    # Check that the values are within the valid RGB range [0, 255]
    for pixel in colored_pixels:
        assert all(0 <= channel <= 255 for channel in pixel)


def test_apply_colormap_empty():
    # Test with an empty list of pixels
    pixels = []
    colored_pixels = apply_colormap(pixels)

    # The result should be an empty list
    assert len(colored_pixels) == 0


def test_apply_colormap_invalid_name():
    # Test with an invalid colormap name
    pixels = [0, 127, 255]

    with pytest.raises(ValueError):
        apply_colormap(pixels, colormap_name="invalid_colormap")


# Test with large data
def test_apply_colormap_large_data():
    pixels = np.random.randint(0, 256, size=1000).tolist()  # 1000 random pixel values

    # Apply a colormap
    colored_pixels = apply_colormap(pixels, colormap_name="inferno")

    # Ensure the output length matches the input
    assert len(colored_pixels) == len(pixels)
    assert len(colored_pixels[0]) == 3  # RGB format

