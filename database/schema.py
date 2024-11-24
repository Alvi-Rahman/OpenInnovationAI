"""
File for database schema definition
Created on Sun Nov 24
Author @TakrimRahmanAlbi
"""
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ImageFrame:
    depth: float
    pixels: List[float]
    colored_pixels: Optional[List[List[int | float]]] = field(default=None)
