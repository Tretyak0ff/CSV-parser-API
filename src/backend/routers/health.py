from fastapi import APIRouter
from loguru import logger

router = APIRouter()


@router.get("/health")
async def health_check():
    logger.debug("Health check requested")
    return {"status": "ok"}
