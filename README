# Prueba Tecnica Savant


El siguiente repositorio es utilizado para una prueba tecnica de Savant para la posicion QA automation


# Estructure del proyecto

El servicio cuenta principalmenet con dos directorios, `src` y `tests`.

1) `src` se encuentra el codigo fuente
2) `test` los casos de prueba


## Arquitectura

El servicio esta disenado para proveer 2 funcionalidades principales

1) Convertir texto a archivo de audio
2) Convertir archivos de audio a text.

Para poder servir estas funcionalidades, el servicio tiene la siguiente estructra:


```
src/
    - api/
        - endpoints/
            - speech/
            - text/
    - app/
    - schema/
```

## `app`

Tiene toda la logica del servidor, funciones de implementacion de texto a audio y audio a text. Para lograr estas funcionalidades, se utilizaron las siguientes librearias

1. whisper [Speech recognition model](https://github.com/openai/whisper)
2. pyttsx3 [Offline Text To Speech](https://github.com/nateshmbhat/pyttsx3)


## `api/endpoints`

Este directorio contiene toda la implemenetacion de los endpoints, no contiene la logic. Solo la definicion de FastApi para los endpoints

Actualmente existe 3 Endpoints:

## `schema`:
En este directorio tenemos todas las definiciones de datos, se utiliza pydantic para definir validaciones y restricciones de datos.

# Instalacion

1. Clonar el repositorios

    ```
    git clone https://github.com/svelezsaffon/savant.git
    ```
2. Ir al directirio

    ```
    cd savant
    ```
3. Crear un ambiente virtual

    ```
    python3 -m venv .venv
    ```

 4. Activar el ambiente virtual

    ```
     source .venv/bin/activate
    ```

# Ejecucion

El proyecto tiene algunas dependencias para ejecutar los modelos de reconicimoento de texto y audio, por lo tanto se sugiere utilizar docker o postman, y ejecutarse en contenedores.

Para faciliar la ejecuion del proyecto, se provee un make file

## Contruir el contenedor

make file
```
make build
```

directamenete
```
docker build -f Dockerfile . -t savant
```

## Ejecturar el contenedor

make file
```
make run
```

directamenete
```
docker run -p 8100:8100 savant:latest
```

## Ejecutar pruebas en docker y afuera

make file
```
make test
```

Dirtectarmenete
```
pytest
```

