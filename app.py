"""
File for App starting point
Created on Sun Nov 24
Author @TakrimRahmanAlbi
"""
from dotenv import load_dotenv
from fastapi import FastAPI
from routes.image_routes import router as frame_router

load_dotenv()
app = FastAPI()
app.include_router(frame_router)
