from fastapi import APIRouter, status
from src.schema.schema import LanguageModel, Language, HealthModel, ServerStatus
from src.api.endpoints import speech, text

api_router = APIRouter()


@api_router.get("/languages", response_model=list[LanguageModel], status_code=status.HTTP_200_OK)
async def read_languages():
    response: list[LanguageModel] = []
    for lang in Language:
        response.append(LanguageModel(name=lang))
    return response


@api_router.get("/health", response_model=HealthModel, status_code=status.HTTP_200_OK)
async def read_languages():
    return HealthModel(status=ServerStatus.READY, ok=True)


api_router.include_router(
    speech.router,
    prefix="/speech",
    tags=["speech"]
)

api_router.include_router(
    text.router,
    prefix="/text",
    tags=["text"]
)
