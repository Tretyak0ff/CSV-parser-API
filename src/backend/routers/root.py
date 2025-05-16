from fastapi import APIRouter
from loguru import logger
from backend.config import settings

router = APIRouter()


@router.get("/")
async def root():
    return {
        "message": "Welcome to CSV Parser API",
        "version": settings.VERSION
    }

