import os
import unittest

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

        self.api_url = os.getenv("API_URL")

        self.speech_url = f"{self.api_url}/api/speech/totext"
        self.text_url = f"{self.api_url}/api/text/toaudio"

    def test_static_text(self):
        body = {
            "rate": 130,
            "text": "call emergency.",
            "volume": 1.5,
            "file_name": "emergency"
        }

        audio_file = requests.post(self.text_url, json=body)

        self.assertEqual(audio_file.status_code, 200)

        audio_text_response = requests.post(
            self.speech_url,
            files={
                "file": (
                    "result.wav",
                    audio_file.content,
                    audio_file.headers.get("content-type", "multipart/form-data")
                )
            }
        )

        self.assertEqual(audio_file.status_code, 200)

        response_data = audio_text_response.json()

        self.assertIn("text", response_data)

        print("----Results---")
        print(f"Current = {response_data['text']}")
        print(f"Expected= {body['text']}")

        self.assertGreaterEqual(
            similarity(response_data["text"], body["text"]),
            self.expected_ratio_static,
            f"{response_data['text']} != {body['text']}"
        )

    def test_mocked_text(self):
        all_text = self.fake.texts(nb_texts=2)

        for text in all_text:
            body = {
                "rate": 130,
                "text": text[:400],
                "volume": 1.5,
                "file_name": "test"
            }

            audio_file = requests.post(self.text_url, json=body)

            self.assertEqual(audio_file.status_code, 200)

            audio_text_response = requests.post(
                self.speech_url,
                files={
                    "file": (
                        "result.wav",
                        audio_file.content,
                        audio_file.headers.get("content-type", "multipart/form-data")
                    )
                }
            )

            self.assertEqual(audio_file.status_code, 200)

            response_data = audio_text_response.json()

            self.assertIn("text", response_data)

            print("----Results---")
            print(f"Current = {response_data['text']}")
            print(f"Expected= {body['text']}")

            self.assertGreaterEqual(
                similarity(response_data["text"], body["text"]),
                self.expected_ratio,
                f"{response_data['text']} != {body['text']}"
            )

    def test_name_and_numbers_flaky(self):
        """
        Prueba textos con nombres y numeros, lo cual lo hace muy inestable
        :return:
        """
        body = {
            "text": f"{self.fake.name()} is 38 years old and has 3 daughters",
            "file_name": "numbers and names"
        }

        audio_file = requests.post(self.text_url, json=body)

        self.assertEqual(audio_file.status_code, 200)

        audio_text_response = requests.post(
            self.speech_url,
            files={
                "file": (
                    "result.wav",
                    audio_file.content,
                    audio_file.headers.get("content-type", "multipart/form-data")
                )
            }
        )

        self.assertEqual(audio_file.status_code, 200)

        response_data = audio_text_response.json()

        self.assertIn("text", response_data)

        print("----Results---")
        print(f"Current = {response_data['text']}")
        print(f"Expected= {body['text']}")

        self.assertGreaterEqual(
            similarity(response_data["text"], body["text"]),
            self.expected_ratio_static,
            f"{response_data['text']} != {body['text']}"
        )
