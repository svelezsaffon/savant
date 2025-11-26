import os
import unittest
import time
import requests
from dotenv import load_dotenv
from difflib import SequenceMatcher
from faker import Faker


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


class TestSpeechUnitCases(unittest.TestCase):

    def setUp(self) -> None:
        """
        Metodo para iniciar/setup los test cases
        :return:
        """
        self.fake = Faker()
        self.expected_ratio = 0.6
        self.expected_ratio_static = 0.91

        load_dotenv()

        self.api_url = os.getenv("API_URL","http://localhost:8100")

        self.to_text_url = f"{self.api_url}/api/speech/totext"
        self.to_audio_url = f"{self.api_url}/api/text/toaudio"

    def test_response_time_text_to_audio(self):
        mocked_text = self.fake.texts(nb_texts=1)[0]

        body = {
            "rate": 130,
            "text": mocked_text,
            "volume": 1.5,
            "file_name": "simple"
        }
        start = time.perf_counter() * 1000

        audio_file = requests.post(self.to_audio_url, json=body)

        self.assertEqual(audio_file.status_code, 200)

        end = time.perf_counter() * 1000

        elapsed = end - start

        self.assertLess(elapsed, 500, f"Text to audio response time fue mayor a 500 {elapsed}")
