from fastapi import Query
from backend.core.factory import FileParserFactory


async def get_parser(file_type: str = Query("csv")):
    return FileParserFactory.get_parser(file_type)
