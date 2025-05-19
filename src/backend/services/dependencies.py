from fastapi import Query
from backend.services.factory import FileParserFactory


async def get_parser(file_type: str = Query("csv")):
    return FileParserFactory.get_parser(file_type)
