"""
File for colormap utils functions
Created on Sun Nov 24
Author @TakrimRahmanAlbi
"""
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize


def get_normalized_pixels(pixels: list):
    """
    :param pixels: list of
    :return: normalized pixel list
    """
    # Convert pixel values to a numpy array
    pixel_array = np.array(pixels)

    # Normalize pixel values to range [0, 1]
    norm = Normalize(vmin=0, vmax=255)
    normalized_pixels = norm(pixel_array)
    return normalized_pixels


def apply_colormap(pixels: list, colormap_name: str = "viridis"):
    """
    Apply a colormap to a 1D list of pixel values.

    :param pixels: 1D list of pixel
    :param colormap_name: name of the colormap to be applied
    :return: 2D list of colormap pixel values after applying colormap
    """
    normalized_pixels = get_normalized_pixels(pixels)
    # Get the colormap
    colormap = cm.get_cmap(colormap_name)

    # Apply the colormap and convert RGBA to RGB (drop alpha channel)
    colored_pixels = colormap(normalized_pixels)[:, :3]  # Shape (n, 3)

    # Convert RGB values (0.0-1.0) to 0-255 integer values
    rgb_pixels = (colored_pixels * 255).astype(int)

    # Return as a list of RGB tuples
    return rgb_pixels.tolist()
