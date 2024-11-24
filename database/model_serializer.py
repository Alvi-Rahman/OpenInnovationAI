"""
File for database models serializer
Created on Sun Nov 24
Author @TakrimRahmanAlbi
"""
from typing import List, Mapping

from pymongo.synchronous.cursor import Cursor

from database.schema import ImageFrame
from utils.colormap import apply_colormap


# Helper function to convert MongoDB document to ImageFrame dataclass
def document_to_image_frame(document: Mapping[str, float | int | str | list], colormap: str) -> ImageFrame:
    """
    Converts a document to a ImageFrame object
    :param document: a mongo document to convert
    :param colormap: colormap used to convert image
    :return: ImageFrame object
    """
    return ImageFrame(depth=document['depth'], pixels=document['pixels'], colored_pixels=apply_colormap(document['pixels'], colormap))


def documents_to_image_frames(documents: Cursor[Mapping[str, float | int | str | list | None]], colormap: str) -> List[ImageFrame]:
    """
    Convert a list of MongoDB documents to a list of ImageFrame dataclasses.
    :param documents: list of MongoDB documents from a specific collection
    :param colormap: Colormap that is to be applied
    """
    return [document_to_image_frame(doc, colormap) for doc in documents]

