from typing import Dict, Any

DESCRIPTION = """
    API helps you do awesome stuff.
    ## Items
    You can **read items**.
    ## Users
    You will be able to:
    * **Create** (_not implemented_).
    * **Read** (_not implemented_).
    """


API_METADATA: Dict[str, Any] = {
    "title": "CSV parser API",
    "description": DESCRIPTION,
    "version": "0.3.0",
    "debug": True,
    "root_path": "/proxy/8889/",
    "docs_url": "/docs",
    "redoc_url": "/redoc",
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


SERVER_SETTINGS = {"host": "0.0.0.0", "port": 8889, "reload": True}


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
