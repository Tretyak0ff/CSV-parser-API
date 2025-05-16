from fastapi import APIRouter, UploadFile, File, Query, Depends
from fastapi.responses import JSONResponse
from loguru import logger
from backend.core.dependencies import get_parser
from backend.core.config import settings
from backend.services.csv_parser import CSVParser
from backend.services.excel_parser import ExcelParser


router = APIRouter()


@router.post("/upload/")
async def upload_file(
    file: UploadFile = File(...),
    parser=Depends(get_parser),
    sheet_name: str = Query(None),
    header_row: int = Query(0),
    encoding: str = Query(settings.DEFAULT_ENCODING),
    delimiter: str = Query(settings.DEFAULT_DELIMITER),
):
    try:
        parser_params = {
            "encoding": encoding,
            "delimiter": delimiter,
            "sheet_name": sheet_name,
            "header_row": header_row,
        }

        # Фильтруем параметры под конкретный процессор
        valid_params = {
            k: v
            for k, v in parser_params.items()
            if k in parser.process.__code__.co_varnames
        }

        result = await parser.process(file, **valid_params)

        logger.success(f"Successfully processed file: {file.filename}")
        return {"success": True, "result": result}
    except Exception as e:
        logger.exception("Critical processing error")
        return JSONResponse(
            status_code=500, content={"success": False, "error": str(e)}
        )
