import csv
import io
from fastapi import HTTPException, status
from loguru import logger
from backend.config import settings



class CSVParser:
    async def process(
        self,
        file,
        encoding: str = settings.DEFAULT_ENCODING,
        delimiter: str = settings.DEFAULT_DELIMITER,
        **kwargs,
    ):
        await self.validate_file(
            file,
            max_size=settings.CSV_MAX_SIZE,
            allowed_types=settings.CSV_ALLOWED_MIME_TYPES,
        )

        try:
            stream = io.TextIOWrapper(file.file, encoding=encoding)
            return await self._process_stream(stream, delimiter)
        except csv.Error as e:
            logger.error(f"CSV processing error: {str(e)}")
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST, detail=f"CSV parsing error: {str(e)}"
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

    async def _process_stream(self, stream, delimiter: str):
        reader = csv.DictReader(stream, delimiter=delimiter)
        data = []
        async for row in self._async_read(reader):
            if len(data) >= settings.OUTPUT_ROW_LIMIT:
                break
            data.append(row)
        return {
            "filename": stream.name,
            "columns": reader.fieldnames,
            "data": data,
            "total_rows": sum(1 for _ in reader),
        }

    async def _async_read(self, reader):
        for row in reader:
            yield row
