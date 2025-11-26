from enum import Enum
from typing import Literal
from pydantic import BaseModel, Field


class Language(str, Enum):
    ES = "ES"
    EN = "EN"
    GE = "GE"


class ServerStatus(str, Enum):
    READY = "ready"


class LanguageModel(BaseModel):
    name: Language = Field(..., description="EL nombre del lenguaje")


class HealthModel(BaseModel):
    status: ServerStatus = Field(..., description="Referencias del status del servedir")
    ok: bool = Field(..., description="El servidor esta ok")

class TextToAudioInput(BaseModel):
    text: str = Field(..., description="Texto a transcribir a audio", min_length=3, max_length=400)
    rate: float = Field(default=125.0, description="Voice Rate", gt=0)
    volume: float = Field(default=1.0, description="Voice Volume", gt=0)
    file_name: str = Field(..., description="Nombre del archivo")
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "Call medical emergency please",
                    "rate": 130.0,
                    "volume": 1.5,
                }
            ]
        }
    }


class AudioToTextModel(BaseModel):
    text: str = Field(..., description="El texto resultante de un audio")
