import pytest
from pydantic import ValidationError

from models.response_models import FrameResponse, FramesListResponse, ErrorResponse


# Test FrameResponse model
@pytest.mark.parametrize(
    "depth, pixels, colored_pixels, is_valid",
    [
        (1.0, [0.0, 127.0, 255.0], [[0, 0, 0], [255, 255, 255]], True),  # Valid data
        (2.5, [10.0, 50.0, 100.0], [[0.1, 0.2, 0.3], [0.5, 0.5, 0.5]], True),  # Valid data
        ("string", [0.0, 127.0, 255.0], [[0, 0, 0], [255, 255, 255]], False),  # Invalid depth (string instead of float)
        (1.0, [0.0, 127.0, "string"], [[0, 0, 0], [255, 255, 255]], False),  # Invalid pixel (string instead of float)
        (1.0, [0.0, 127.0, 255.0], "invalid", False),  # Invalid colored_pixels (should be a list of lists)
    ]
)
def test_frame_response(depth, pixels, colored_pixels, is_valid):
    if is_valid:
        # If data is valid, expect successful validation
        frame = FrameResponse(depth=depth, pixels=pixels, colored_pixels=colored_pixels)
        assert frame.depth == depth
        assert frame.pixels == pixels
        assert frame.colored_pixels == colored_pixels
    else:
        # If data is invalid, expect a ValidationError
        with pytest.raises(ValidationError):
            FrameResponse(depth=depth, pixels=pixels, colored_pixels=colored_pixels)


# Test FramesListResponse model
@pytest.mark.parametrize(
    "frames_data, is_valid",
    [
        ([{"depth": 1.0, "pixels": [0.0, 127.0, 255.0], "colored_pixels": [[0, 0, 0], [255, 255, 255]]}], True),  # Valid data
        ([{"depth": "string", "pixels": [0.0, 127.0, 255.0], "colored_pixels": [[0, 0, 0], [255, 255, 255]]}], False),  # Invalid depth
        ([{"depth": 1.0, "pixels": [0.0, 127.0, 255.0], "colored_pixels": "invalid"}], False),  # Invalid colored_pixels
        ([], True),  # Empty list (valid case)
    ]
)
def test_frames_list_response(frames_data, is_valid):
    if is_valid:
        # If data is valid, expect successful validation
        frames_list = FramesListResponse(frames=frames_data)
        assert len(frames_list.frames) == len(frames_data)
    else:
        # If data is invalid, expect a ValidationError
        with pytest.raises(ValidationError):
            FramesListResponse(frames=frames_data)


# Test ErrorResponse model
@pytest.mark.parametrize(
    "message, error_type, input_data, is_valid",
    [
        ("Some error occurred", "ValidationError", {"field": "value"}, True),  # Valid data
        ("Some error occurred", "ValidationError", [], True),  # Valid empty list
        ("Some error occurred", "ValidationError", "invalid", False),  # Invalid input data type (should be dict or list)
        (None, "ValidationError", {"field": "value"}, False),  # Invalid message (None is not allowed)
        ("Some error occurred", None, {"field": "value"}, False),  # Invalid type (None is not allowed)
    ]
)
def test_error_response(message, error_type, input_data, is_valid):
    if is_valid:
        # If data is valid, expect successful validation
        error_response = ErrorResponse(message=message, type=error_type, input=input_data)
        assert error_response.message == message
        assert error_response.type == error_type
        assert error_response.input == input_data
    else:
        # If data is invalid, expect a ValidationError
        with pytest.raises(ValidationError):
            ErrorResponse(message=message, type=error_type, input=input_data)

