from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.api.router import api_router


async def manage_all_exception(request: Request, exc: Exception) -> JSONResponse:
    """
    Maneja excepciones generales del
    :param request: el request de FastAPi
    :param exc: La exception que fue lanzada
    :return: Js
    """

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": str(exc),
            "request": request.body()
        }
    )


def create_application() -> FastAPI:
    app = FastAPI(
        title="Santiago Velez && Savant",
        description="APi para prueba tecnica en Savant"
    )

    origins = [
        "http://localhost",
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(api_router, prefix="/api")

    app.add_exception_handler(Exception, manage_all_exception)
    return app


app = create_application()
