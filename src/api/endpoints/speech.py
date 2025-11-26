"""
Este archivo contiene todos los endpoints relacionados a funciones de voz
"""
from typing import Annotated
import tempfile

from fastapi import APIRouter, status, UploadFile
from src.schema.schema import AudioToTextModel
from src.app.logic import audio_to_text

router = APIRouter()


@router.post("/totext", status_code=status.HTTP_201_CREATED, response_model=AudioToTextModel)
async def get_text(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False, suffix=file.filename) as tmp:
        temp_path = tmp.name
        contents = await file.read()
        tmp.write(contents)

    text = audio_to_text(temp_path)

    return AudioToTextModel(text=text)
