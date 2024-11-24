"""
File for preprocessing of data
Created on Sun Nov 24
Author @TakrimRahmanAlbi
"""
import pandas as pd
from scipy.ndimage import zoom


def resize_pixels(row: pd.Series, target_width: int = 150, original_width: int = 200):
    """
    Resize the pixels of a series of images to target width
    :param row:
    :param target_width:
    :param original_width:
    :return:
    """
    return zoom(row, target_width / original_width)


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Resize the data to fit the required dimensions
    :param data:
    :return:
    """
    depth_column = data['depth']
    pixel_data = data.iloc[:, 1:]
    resized_pixel_data = pixel_data.apply(lambda row: resize_pixels(row.values), axis=1)
    resized_pixel_df = pd.DataFrame(resized_pixel_data.tolist(), columns=[f'pixel_{i + 1}' for i in range(150)])
    resized_data = pd.concat([depth_column, resized_pixel_df], axis=1)
    return resized_data
