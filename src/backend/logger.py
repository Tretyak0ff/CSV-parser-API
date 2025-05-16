from loguru import logger
import sys

def setup_logging():
    if not logger._core.handlers:
        logger.remove()  # Удаляем все существующие обработчики
        logger.add(
            sys.stderr,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
            level="INFO",
            enqueue=True
        )
        logger.add(
            "backend.log",
            rotation="10 MB",
            retention="7 days",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
            level="INFO",
            enqueue=True
        )
    return logger

logger = setup_logging()
