"""
File for request object model definitions
Created on Sun Nov 24
Author @TakrimRahmanAlbi
"""
from fastapi import Query
from pydantic import BaseModel, field_validator, model_validator
import _constants as C


class FrameRequest(BaseModel):
    depth_min: float = Query(..., description="Minimum depth value")
    depth_max: float = Query(..., description="Maximum depth value")
    limit: int = Query(10, le=100, description="Number of results to return per page")
    skip: int = Query(0, ge=0, description="Number of results to skip (for pagination)")
    colormap: str = Query("viridis", description="Name of the colormap to apply (e.g., 'viridis', 'plasma')")


class FrameRequestValidator(FrameRequest):
    @field_validator("depth_min", "depth_max", mode="before")
    def validate_depth_fields(cls, value, info):
        if value is None:
            raise ValueError(f"{info.field_name} must be non-negative.")
        if value < 0:
            raise ValueError(f"{info.field_name} must be non-negative.")
        return value

    @field_validator("limit", mode="before")
    def validate_limit(cls, value):
        if value <= 0:
            raise ValueError("limit must be greater than 0.")
        return value

    @field_validator("skip", mode="before")
    def validate_skip(cls, value):
        if value < 0:
            raise ValueError("skip must be non-negative.")
        return value

    # Cross-field validation
    @model_validator(mode="before")
    def validate_depth_range(cls, values):
        depth_min = values.get("depth_min")
        depth_max = values.get("depth_max")
        if depth_min is not None and depth_max is not None and depth_min > depth_max:
            raise ValueError("depth_min must be less than or equal to depth_max.")
        return values

    @field_validator("colormap", mode="before")
    def validate_colormap(cls, value):
        valid_colormaps = C.SUPPORTED_COLORMAPS
        if value not in valid_colormaps:
            raise ValueError(f"Invalid colormap name '{value}'. Valid options are: {', '.join(valid_colormaps)}.")
        return value


class UploadRequest(BaseModel):
    file_name: str
