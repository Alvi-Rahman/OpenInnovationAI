"""
File for routes related to image operations
Created on Sun Nov 24
Author @TakrimRahmanAlbi
"""
from fastapi import HTTPException, Depends, APIRouter
from pydantic import ValidationError

from database.config import get_collection, get_mongo_client
from database.model_serializer import documents_to_image_frames
from database.query import get_image_frames, read_and_insert_frames
from models.request_models import FrameRequest, FrameRequestValidator, UploadRequest
from models.response_models import FramesListResponse, FrameResponse
import logging

from utils.errors import format_validation_error

router = APIRouter()
db = get_mongo_client()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.get("/frames")
async def get_frames(
    request: FrameRequest = Depends()
):
    """
    Retrieve frames within the specified depth range from MongoDB.
    """

    # Log the incoming request for debugging and monitoring
    logger.info(f"Received request: {request}")
    try:
        _ = FrameRequestValidator(**request.dict())
    except ValidationError as e:
        raise HTTPException(
            status_code=422,
            detail=format_validation_error(e)
        )
    try:
        # Query MongoDB for frames within the depth range, with pagination
        image_data_collection = get_collection(db, "image_data")
        results = get_image_frames(image_data_collection, request.depth_min, request.depth_max, request.limit, request.skip)
        # Convert MongoDB documents to ImageFrame dataclasses
        frames = documents_to_image_frames(results, request.colormap)

        # Convert dataclass list to Pydantic models for response serialization
        frame_responses = [FrameResponse(depth=frame.depth, pixels=frame.pixels, colored_pixels=frame.colored_pixels) for frame in frames]

        return FramesListResponse(frames=frame_responses)
    # Handling generic exception. can be more specific in terms of handling more granular error
    except Exception as e:
        logger.error(f"Error fetching frames: {str(e)}")
        raise HTTPException(
            status_code=400,
            detail="An error occurred"
        )


@router.post("/upload/")
async def upload_data(
    request: UploadRequest
):
    """
    Uploads data into mongoDB
    """

    # Log the incoming request for debugging and monitoring
    logger.info(f"Received request: {request}")
    try:
        # Query MongoDB for frames within the depth range, with pagination
        image_data_collection = get_collection(db, "image_data")
        try:
            return read_and_insert_frames(image_data_collection, request.file_name)
        except ValueError as e:
            logger.error(f"Error reading file: {str(e)}")
            raise HTTPException(
                status_code=400,
                detail="File doesn't exist"
            )
    # Handling generic exception. can be more specific in terms of handling more granular error
    except Exception as e:
        logger.error(f"Error reading file: {str(e)}")
        raise HTTPException(
            status_code=400,
            detail="An error occurred"
        )
