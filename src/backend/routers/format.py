from fastapi import APIRouter
from loguru import logger
from backend.services.factory import FileParserFactory

router = APIRouter()


@router.get("/format")
async def supported_formats():
    logger.info("Request received for supported formats")
    return {"supported_formats": list(FileParserFactory._parser.keys())}
