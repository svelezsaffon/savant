from enum import Enum
from typing import Literal
from pydantic import BaseModel, Field


class Language(str, Enum):
    ES = "ES"
    EN = "EN"
    GE = "GE"


class LanguageModel(BaseModel):
    name: Language = Field(..., description="EL nombre del lenguaje")


