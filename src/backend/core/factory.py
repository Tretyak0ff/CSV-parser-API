from loguru import logger
from fastapi import HTTPException, status


class FileParserFactory:
    _parser = {}

    @classmethod
    def register(cls, name: str, parser):
        cls._parser[name.lower()] = parser
        logger.info(f"Registered parser: {name}")

    @classmethod
    def get_parser(cls, file_type: str):
        parser = cls._parser.get(file_type.lower())
        if not parser:
            logger.warning(f"Attempt to access unknown parser: {file_type}")
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail=f"Unsupported file type: {file_type}",
            )
        return parser


from backend.core.csv_parser import CSVParser

FileParserFactory.register("csv", CSVParser())

from backend.core.excel_parser import ExcelParser

FileParserFactory.register("xls", ExcelParser())
FileParserFactory.register("xlsx", ExcelParser())
