from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from uvicorn import run
from backend.exceptions import handle_http_exception
from backend.routers.health import router as health_router
from backend.routers.root import router as root
from backend.routers.format import router as formats_router
from backend.routers.upload import router as upload_router
from backend.core.config import settings


app = FastAPI(**settings.metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.add_exception_handler(HTTPException, handle_http_exception)
app.include_router(root)
app.include_router(upload_router)
app.include_router(health_router)
app.include_router(formats_router)


def start():
    logger.info("Starting application...")
    run(
        "src.backend.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        log_config=None,
    )


if __name__ == "__main__":
    start()
