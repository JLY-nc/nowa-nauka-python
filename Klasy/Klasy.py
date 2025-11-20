### Czym jest klasa?
# Bez klas - dane i funkcje są osobno
name = "OpenAI"
model = "gpt-4o-mini"


def generate_response(prompt):
    # Przetwarzanie promptu...
    return response


# Z klasami - Wszystko jest spakowane razem
class OpenAIClient:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def generate_response(self, prompt):
        # Przetwarzanie promptu...
        return response


### Typowa progresja dewelopera Pythona
## 1. Pojedynczy skrypt w pliku
# wszystko.py - cały kod w pojedynczym pliku
api_key = "sk-..."
prompt = "Wyjaśnij Python"
response = make_api_call(api_key, prompt)
print(response)


## 2. Funkcje
# główny.py - zorganizowany plik dzięki funkcjom
def setup_api(key):
    return {"key": key, "base_url": "https://api.openai.com"}


def generate_response(api_config, prompt):
    # Zapytanie API
    return response


api = setup_api("sk-...")
result = generate_response(api, "Wyjaśnij python")


## 3. Wiele plików
# api_utils.py
def setup_api(key):
    return {"key": key, "base_url": "https://api.openai.com"}


# main.py
from api_utils import setup_api

api = setup_api("sk-...")


## 4. Klasy
# client.py
class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openai.com"

    def generate(self, prompt):
        # Cała logika jest zamknięta w kapsułce
        return response


# main.py
from client import OpenAIClient

client = OpenAIClient("sk-...")
response = client.generate("Wyjaśnij Python")
