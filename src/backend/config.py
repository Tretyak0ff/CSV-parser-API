import os
from dotenv import load_dotenv
from typing import Dict, Any
from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger

load_dotenv()

DESCRIPTION = (
    f"API helps you do awesome stuff."
    f"\n## Items"
    f"\nYou can read **CSV** & **Excel** files."
)


API_METADATA: Dict[str, Any] = {
    "title": "CSV parser API",
    "description": DESCRIPTION,
    "version": "0.3.1",
    "debug": os.getenv("DEBUG"),
    "root_path": os.getenv("ROOT_PATH"),
    "docs_url": os.getenv("DOCS_URL"),
    "redoc_url": os.getenv("REDOC_URL"),
    "summary": "Deadpool's favorite app. Nuff said.",
    "contact": {
        "name": "Evgen Tretyakov",
        "email": "evgentretyakoff@gmail.com",
    },
    "license_info": {
        "name": "MIT License",
        "url": "https://mit-license.org/",
    },
}


SERVER_SETTINGS = {
    "host": os.getenv("HOST"),
    "port": int(os.getenv("PORT")),
    "reload": os.getenv("RELOAD"),
}


class AppConfig:
    # CSV settings
    CSV_MAX_SIZE = 20 * 1024 * 1024  # 20MB
    CSV_ALLOWED_MIME_TYPES = {"text/csv", "application/vnd.ms-excel"}

    # Excel settings
    EXCEL_MAX_SIZE = 50 * 1024 * 1024  # 50MB
    EXCEL_ALLOWED_MIME_TYPES = {
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/vnd.ms-excel",
    }

    # Common settings
    DEFAULT_ENCODING = "utf-8"
    DEFAULT_DELIMITER = ";"
    OUTPUT_ROW_LIMIT = 100


config = AppConfig()


class AppSettings(BaseSettings):

    # DB_URL: str
    # SECRET_KEY: str

    DEBUG: bool = os.getenv("DEBUG"),
    RELOAD: bool = os.getenv("RELOAD"),

    HOST: str = os.getenv("HOST")
    PORT: int = int(os.getenv("PORT"))
    
    ROOT_PATH: str = os.getenv("ROOT_PATH")
    DOCS_URL: str = os.getenv("DOCS_URL")
    REDOC_URL: str = os.getenv("REDOC_URL")
    
    # Параметры с дефолтными значениями
    # DEBUG: bool = False
    # HOST: str = "localhost"
    # PORT: int = 8000



    # Конфигурация должна быть объявлена через SettingsConfigDict
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        # env_prefix="APP_",  # Все переменные должны начинаться с APP_
        # case_sensitive=False
    )

# Инициализация конфига (лучше через вызов экземпляра)
settings = AppSettings()

logger.debug(settings)
