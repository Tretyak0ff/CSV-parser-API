from fastapi import HTTPException
from fastapi.responses import JSONResponse
from loguru import logger


async def handle_http_exception(request, exc):
    logger.error(f"HTTP error [{exc.status_code}]: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code, content={"success": False, "error": exc.detail}
    )
