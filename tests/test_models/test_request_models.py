import pytest
from pydantic import ValidationError
from models.request_models import FrameRequestValidator, FrameRequest, UploadRequest


# Test FrameRequestValidator Model (parametric tests)
@pytest.mark.parametrize(
    "depth_min, depth_max, limit, skip, colormap, is_valid",
    [
        (0.0, 10.0, 10, 0, "viridis", True),  # Valid case
        (5.0, 10.0, 10, 0, "plasma", True),  # Valid case
        (0.0, 10.0, 0, 0, "viridis", False),  # Invalid limit (0 is not allowed)
        (10.0, 5.0, 10, 0, "viridis", False),  # Invalid depth range (depth_min > depth_max)
        (0.0, -5.0, 10, 0, "viridis", False),  # Invalid depth_max (negative value)
        (-1.0, 10.0, 10, 0, "viridis", False),  # Invalid depth_min (negative value)
        (0.0, 10.0, 10, -1, "viridis", False),  # Invalid skip (negative value)
        (0.0, 10.0, 10, 0, "invalid_colormap", False),  # Invalid colormap (not in the list)
    ]
)
def test_frame_request_validator(depth_min, depth_max, limit, skip, colormap, is_valid):
    if is_valid:
        # If data is valid, expect successful validation
        frame_request = FrameRequestValidator(
            depth_min=depth_min, depth_max=depth_max, limit=limit, skip=skip, colormap=colormap
        )
        assert frame_request.depth_min == depth_min
        assert frame_request.depth_max == depth_max
        assert frame_request.limit == limit
        assert frame_request.skip == skip
        assert frame_request.colormap == colormap
    else:
        # If data is invalid, expect a ValidationError
        with pytest.raises(ValidationError):
            FrameRequestValidator(
                depth_min=depth_min, depth_max=depth_max, limit=limit, skip=skip, colormap=colormap
            )


# Test FrameRequest Model (without validators)
@pytest.mark.parametrize(
    "depth_min, depth_max, limit, skip, colormap, is_valid",
    [
        (0.0, 10.0, 10, 0, "viridis", True),  # Valid case
        (5.0, 10.0, 10, 0, "plasma", True),  # Valid case
        (0.0, 10.0, 0, 0, "viridis", True),  # Limit of 0 is allowed in FrameRequest (since no validation in this model)
        (10.0, 5.0, 10, 0, "viridis", True),  # Valid case, no validation for depth range in FrameRequest
        (-1.0, 10.0, 10, 0, "viridis", True),  # Invalid depth_min (negative value), but FrameRequest has no validation
    ]
)
def test_frame_request(depth_min, depth_max, limit, skip, colormap, is_valid):
    if is_valid:
        # If data is valid, expect successful validation
        frame_request = FrameRequest(
            depth_min=depth_min, depth_max=depth_max, limit=limit, skip=skip, colormap=colormap
        )
        assert frame_request.depth_min == depth_min
        assert frame_request.depth_max == depth_max
        assert frame_request.limit == limit
        assert frame_request.skip == skip
        assert frame_request.colormap == colormap
    else:
        # If data is invalid, expect a ValidationError
        with pytest.raises(ValidationError):
            FrameRequest(
                depth_min=depth_min, depth_max=depth_max, limit=limit, skip=skip, colormap=colormap
            )


# Test UploadRequest Model
@pytest.mark.parametrize(
    "file_name, is_valid",
    [
        ("image.csv", True),  # Valid case
        ("", True),  # Empty file name
        (None, False),  # None as file name
    ]
)
def test_upload_request(file_name, is_valid):
    if is_valid:
        # If data is valid, expect successful validation
        upload_request = UploadRequest(file_name=file_name)
        assert upload_request.file_name == file_name
    else:
        # If data is invalid, expect a ValidationError
        with pytest.raises(ValidationError):
            UploadRequest(file_name=file_name)
