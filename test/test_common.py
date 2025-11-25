import unittest
import uuid

import requests

from src.schema.schema import LanguageModel

from dotenv import load_dotenv
import os


class TestSpeeech(unittest.TestCase):

    def setUp(self) -> None:
        """
        Metodo para iniciar/setup los test cases
        :return:
        """
        load_dotenv()

        self.api_url = os.getenv("API_URL")

        self.lang_url = f"{self.api_url}/api"

    def test_read_language_response_code(self):
        """
        Verifica endpoint para leer los lenguajes disponibles
        :return:
        """
        lang = requests.get(f"{self.lang_url}/languages")

        self.assertEqual(lang.status_code, 200, "El endpoint languages, no responde con 200")

    def test_read_language_response_values(self):
        """
        Verifica que existan lenguajes disponibles
        :return:
        """
        languages = requests.get(f"{self.lang_url}/languages").json()

        self.assertTrue(len(languages) > 0, "No hay lenguajes disponibles")

        for language in languages:
            try:
                # Utilicemos a pydantic para validaciond e datos :)
                LanguageModel(**language)
            except Exception as e:
                self.fail(str(e))

    def test_random_endpoint_404(self):
        """
        Verifica que el servidor responda 404 cuando se utiliza un endpoijnt que no existe
        :return:
        """

        lang = requests.get(f"{self.lang_url}/{str(uuid.uuid4())}")

        self.assertEqual(lang.status_code, 404)
