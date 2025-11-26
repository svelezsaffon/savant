"""
Este archivo contiene todos los endpoints relacionados a funciones de text
"""
from typing import Annotated
from fastapi import APIRouter, status, Body
from fastapi.responses import FileResponse, JSONResponse
from src.schema.schema import LanguageModel, Language, TextToAudioInput

from src.app.logic import text_to_audio

router = APIRouter()


@router.post("/toaudio", response_model=None, status_code=status.HTTP_201_CREATED)
async def text_to_speech(text_props: Annotated[TextToAudioInput, Body()]):
    file_path = text_to_audio(text_props=text_props)
    return FileResponse(
        file_path,
        media_type="audio/mpeg",
        filename="audio.mp3"
    )