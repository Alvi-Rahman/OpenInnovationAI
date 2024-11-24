"""
File for response object model definitions
Created on Sun Nov 24
Author @TakrimRahmanAlbi
"""
from pydantic import BaseModel
from typing import List


class FrameResponse(BaseModel):
    depth: float
    pixels: List[float]
    colored_pixels: List[List[int | float]]


class FramesListResponse(BaseModel):
    frames: List[FrameResponse]


class ErrorResponse(BaseModel):
    message: str
    type: str
    input: dict | list
