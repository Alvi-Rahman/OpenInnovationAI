"""
File for defining constants
Created on Sun Nov 24
Author @TakrimRahmanAlbi
"""
import os

from dotenv import load_dotenv

load_dotenv()
SUPPORTED_COLORMAPS = ["viridis", "plasma", "inferno", "magma", "cividis"]
MONGODB_LOCAL_URI = os.getenv("MONGODB_LOCAL_URI", "mongodb://host.docker.internal:27017/")
MONGODB_DOCKER_URI = os.getenv("MONGODB_DOCKER_URI", "mongodb://localhost:27017/")
docker_mode = os.getenv("DOCKER", 'False')
if eval(docker_mode):
    MONGODB_URI = MONGODB_LOCAL_URI
else:
    MONGODB_URI = MONGODB_DOCKER_URI
MONGODB_DATABASE = os.getenv("DB_NAME", "OpenInnovationAIImageDB")
IMG_DATA_PATH = os.getenv("IMG_DATA_PATH", "data")
