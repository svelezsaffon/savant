import os
import unittest

import requests
from dotenv import load_dotenv
from difflib import SequenceMatcher
from faker import Faker
from fastapi import status


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


class TestTextToAudio(unittest.TestCase):

    def setUp(self) -> None:
        """
        Metodo para iniciar/setup los test cases
        :return:
        """

        load_dotenv()

        self.api_url = os.getenv("API_URL","http://localhost:8100")

        self.text_url = f"{self.api_url}/api/text/toaudio"

    def test_min_length(self):
        """
        Verifica que el servidor requirea la minima longitud de texto
        :return:
        """
        body = {
            "text": "ab"
        }

        text_audio = requests.post(self.text_url, json=body)

        self.assertEqual(text_audio.status_code, status.HTTP_422_UNPROCESSABLE_CONTENT)

    def test_max_length(self):
        """
        Verifica que el servidor requirea la minima longitud de texto
        :return:
        """
        body = {
            "text": ''.join([str(x) for x in range(0, 401)]),
            "file_name": "chars_400"
        }

        text_audio = requests.post(self.text_url, json=body)

        self.assertEqual(text_audio.status_code, status.HTTP_422_UNPROCESSABLE_CONTENT)

    def test_min_volume(self):
        """
        Verifica que el servidor requirea la minima longitud de texto
        :return:
        """
        body = {
            "text": "this is a text",
            "volume": -2,
            "file_name": "negative_vol"
        }

        text_audio = requests.post(self.text_url, json=body)

        self.assertEqual(text_audio.status_code, status.HTTP_422_UNPROCESSABLE_CONTENT)

    def test_min_tone(self):
        """
        Verifica que el servidor requirea la minima longitud de texto
        :return:
        """
        body = {
            "text": "this is a text",
            "rate": -2,
            "file_name": "negative_rate"
        }

        text_audio = requests.post(self.text_url, json=body)

        self.assertEqual(text_audio.status_code, status.HTTP_422_UNPROCESSABLE_CONTENT)