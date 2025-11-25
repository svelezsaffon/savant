"""
Este archivo contiene todos los endpoints relacionados a funciones de text
"""
from fastapi import APIRouter, status
from src.schema.schema import LanguageModel, Language

router = APIRouter()
