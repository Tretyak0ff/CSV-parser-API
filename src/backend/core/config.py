import os
from dotenv import load_dotenv
from typing import Dict, Any
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger

load_dotenv()


class AppSettings(BaseSettings):
    HOST: str
    PORT: int
    ROOT_PATH: str

    DEBUG: bool = True
    RELOAD: bool = True
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"

    TITLE: str = "CSV parser API"
    DESCRIPTION: str = Field(
        default=(
            f"API helps you do awesome stuff."
            f"\n## Items"
            f"\nYou can read **CSV** & **Excel** files."
        ),
        description="API description in Markdown format",
    )
    VERSION: str = "0.3.1"
    SUMMARY: str = "Deadpool's favorite app. Nuff said."
    CONTACT: dict[str, str] = {
        "name": "Evgen Tretyakov",
        "email": "evgentretyakoff@gmail.com",
    }
    LICENSE_INFO: dict[str, str] = {
        "name": "MIT License",
        "url": "https://mit-license.org/",
    }

    CSV_MAX_SIZE: int = 20 * 1024 * 1024  # 20MB
    CSV_ALLOWED_MIME_TYPES: list[str] = {"text/csv", "application/vnd.ms-excel"}

    EXCEL_MAX_SIZE: int = 50 * 1024 * 1024  # 50MB
    EXCEL_ALLOWED_MIME_TYPES: list[str] = {
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/vnd.ms-excel",
    }

    # Common settings
    DEFAULT_ENCODING: str = "utf-8"
    DEFAULT_DELIMITER: str = ";"
    OUTPUT_ROW_LIMIT: int = 100

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        # extra="ignore",
        # env_prefix="APP_",
    )

    @property
    def metadata(self) -> Dict[str, Any]:
        return {
            "title": self.TITLE,
            "description": self.DESCRIPTION,
            "version": self.VERSION,
            "summary": self.SUMMARY,
            "contact": self.CONTACT,
            "license_info": self.LICENSE_INFO,
            "debug": self.DEBUG,
            "root_path": self.ROOT_PATH,
            "docs_url": self.DOCS_URL,
            "redoc_url": self.REDOC_URL,
        }


settings = AppSettings()
