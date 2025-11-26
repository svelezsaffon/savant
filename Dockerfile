FROM python:3.11-slim

# Dependencias de openapi whisper https://github.com/openai/whisper?tab=readme-ov-file#setup
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ffmpeg \
        espeak \
        espeak-ng \
        libespeak1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8100

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8100"]
