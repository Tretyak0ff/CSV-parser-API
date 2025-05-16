import io
import pandas as pd
from fastapi import HTTPException, status
from loguru import logger
from backend.config import settings



class ExcelParser:
    async def process(
        self,
        file,
        sheet_name: str = "Sheet1",
        header_row: int = 0,
        **kwargs,
    ):
        await self.validate_file(
            file,
            max_size=settings.EXCEL_MAX_SIZE,
            allowed_types=settings.EXCEL_ALLOWED_MIME_TYPES,
        )

        try:
            contents = await file.read()
            df = pd.read_excel(
                io.BytesIO(contents),
                sheet_name=sheet_name,
                header=header_row,
                engine="openpyxl",
            )
            return await self._process_dataframe(df, file.filename)
        except Exception as e:
            logger.error(f"Excel processing error: {str(e)}")
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST, detail=f"Excel parsing error: {str(e)}"
            )
        finally:
            await file.close()

    async def validate_file(self, file, max_size: int, allowed_types: set):
        if file.content_type not in allowed_types:
            raise HTTPException(
                status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="Unsupported file type"
            )

        file.file.seek(0, 2)
        if file_size := file.file.tell() > max_size:
            raise HTTPException(
                status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                detail=f"File size {file_size} exceeds limit {max_size}",
            )
        file.file.seek(0)

    async def _process_dataframe(self, df, filename):
        data = df.head(settings.OUTPUT_ROW_LIMIT).to_dict(orient="records")
        return {
            "filename": filename,
            "columns": df.columns.tolist(),
            "data": data,
            "total_rows": len(df),
            "dtypes": df.dtypes.astype(str).to_dict(),
        }
