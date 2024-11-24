"""
File for database querying
Created on Sun Nov 24
Author @TakrimRahmanAlbi
"""
import os.path
from typing import Mapping

from pymongo.collection import Collection
import pandas as pd
from pymongo.synchronous.cursor import Cursor

from database.schema import ImageFrame
import _constants as C
from utils.preprocess import preprocess_data


# Helper function to insert an ImageFrame into MongoDB
def insert_single_image_frame(collection: Collection, image_frame: ImageFrame):
    """
    Insert single image frame into the collection
    :param collection: Collection Name
    :param image_frame: ImageFrame object
    :return: the inserted document response
    """
    document = {
        'depth': image_frame.depth,
        'pixels': image_frame.pixels
    }
    response = collection.insert_one(document)
    return response


def insert_image_frames(data: pd.DataFrame, collection: Collection):
    """
    Insert multiple image frames into the collection
    :param data: the pandas DF to be inserted into the collection
    :param collection: name of the Collection
    :return: response after insertion
    """
    documents = []
    for _, row in data.iterrows():
        document = {
            "depth": row['depth'],  # Store the depth value
            "pixels": row.iloc[1:].tolist()  # Store the resized pixel data as an array
        }
        documents.append(document)

    # Insert documents into MongoDB collection
    collection.insert_many(documents)

    return {"response": f"{len(documents)} rows inserted"}


def read_and_insert_frames(collection: Collection, file_name: str):
    """
    Read and insert frames into a MongoDB collection
    :param collection: name of the Collection
    :param file_name: name of the File
    :return:
    """
    data_path = os.path.join(C.IMG_DATA_PATH, file_name)
    if not os.path.exists(data_path):
        raise ValueError("File Not Found")
    data = pd.read_csv(data_path)

    filtered_db_data = collection.find({"depth": {"$nin": data["depth"].tolist()}})
    filtered_depths = [data["depth"] for data in filtered_db_data]
    filtered_data = data[data["depth"].isin(filtered_depths)]
    if not filtered_data.shape[0]:
        return {"Response": "No New Frames Found"}
    processed_data = preprocess_data(data)
    return insert_image_frames(processed_data, collection)


def get_image_frames(image_data_collection: Collection, depth_min: float | int, depth_max: float | int, limit: int, skip: int) -> Cursor[Mapping[str, float | int | str | list | None]]:
    """
    Get frames from a MongoDB
    :param image_data_collection: Collection
    :param depth_min: min depth of image
    :param depth_max: max depth value
    :param limit: limit the number of response returned
    :param skip: items to be skipped from the beginning
    :return: Cursor[Mapping[str, float | int | str | list]] of documents
    """
    results = image_data_collection.find(
        {"depth": {"$gte": depth_min, "$lte": depth_max}}
    ).skip(skip).limit(limit)
    return results
