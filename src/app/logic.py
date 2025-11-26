import uuid
import whisper
import pyttsx3
import os

from src.schema.schema import TextToAudioInput

#Carguemos el modelo con el inicio del servidor, asi ahorramos tiempo
model = whisper.load_model("turbo")


def text_to_audio(text_props: TextToAudioInput):
    """
    Convierte una cadena de texto a audio
    :param text_props:
    :return:
    """
    filename = f"{text_props.file_name}.mp3"
    filepath = f"/tmp/{uuid.uuid4()}/{filename}"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    engine = pyttsx3.init()
    engine.setProperty('rate', text_props.rate)
    engine.setProperty('volume', text_props.volume)

    engine.save_to_file(text_props.text, filepath)
    engine.runAndWait()
    engine.stop()
    return filepath


def audio_to_text(file_path):
    """
    Convierte un archivo de audio a un texto
    Esta funcion es copiada del README de github https://github.com/openai/whisper?tab=readme-ov-file#python-usage
    :param file_path:
    :return:
    """
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(file_path)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # print the recognized text
    return result.text
