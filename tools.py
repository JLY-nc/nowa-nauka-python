# Paczki dzielimy na dwa rodzaje:
# Wbudowane to takie, które są od razu z Pythonem
# Zewnętrzne to takie, które nalezy pobrac przy pomocy `pip`
# Terminologia
# Moduł(Module) to pojedynczy plik python, np. `hello.py` -  to skrzynka narzędziowa
# Paczka(Package) to folder zawierający wiele modułów - to garaz z wieloma skrzynkami narzedziowymi
# Funkcje(Function) to wielokrtonie uzywany blok kodowy jak, np. print() lub sqrt() - to jest konkretne narzedzie
# Klasy(Class) to szkic do tworzenia obiektów - a to jest szkic do ktorego zbudowania wykorzystasz narzedzia


# import math - to jest jak wyciagniecie całej skrzynki z narzędziami

# root = math.sqrt(16) - a tutaj uzywamy konkrentego narzedzia

# from math import (
#     sqrt,
#     pi,
# )  # Natomiast w tym przypadku od razu wyciągamy tylko potrzebne narzedzia ze skrzynki

# sqrt(16)
# pi()


# Losowe wartości
# import random

# number = random.randint(1, 10)
# choice = random.choice(["apple", "banana", "orange"])

# Czas i data
# import datetime

# today = datetime.date.today()
# print(today)

# System operacyjny
# import os

# current_dir = os.getcwd() # Zaciąga nam to obecny katalog w którym pracujemy
# print(current_dir)


# Dane w postaci JSON
# import json
# data = {"name": "Alice", "age": 30}
# json_string = json.dumps(data)
# print(json_string)

# Metody importowania
# Import całego modułu
# import math
# result = math.sqrt(16)

# Import konkretnych funkcji
# from math import sqrt, pi
# result = sqrt(16)
# circle_area = pi * radius ** 2

# Import z aliasem, czyli importujemy moduł tak jakby z nickiem, który będzie nam łatwiej uzywac
# import pandas as pd
# df = pd.DataFrame(data)

# Import wszystkiego (UNIKAĆ TEGO!)
# from math import *


# from pydantic import BaseModel

# Gdy pracujemy na tym samym stacku technologicznym warto zrobić sobie plik requirements.txt, który będzie zawierał wszystkie moduły, które znajdują się w danym środowisku - zrobimy to poprzez wpisanie w terminalu `pip freeze > requirements.txt`

# Gdy chcemy zainstalować wszystko z tego dokumentu wystarczy wpisać w terminalu `pip install -r requirements.txt`
# w momencie, gdy zaczynamy prace na nowym projekcie i mamy plik `requirements.txt` to przy tworzeniu środowiska VS Code zapyta czy chcemy równiez zainstalować inne zaleznosci

# Uzywanie zewnetrznych paczek
# Zapytania internetowe
# import requests

# response = requests.get("https://api.example.com/data")
# data = response.json()

# Analiza danych
import pandas as pd

# Prosta struktura danych
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [24, 30, 25],
    "city": ["NYC", "LA", "Chicago"],
}
df = pd.DataFrame(data)
print(df)

# Zawsze warto uzywac wirtulanych srodowisk do projektów. Zapobiega to konfilktom miedzy paczkami

# Gdzie szukac paczek
# PyPI - Oficjalne spis paczek Python
# Awesome Python - Wyselekcjonowana lista paczek
# ChatGPT - Zadaj pytanie "Jakiej paczki Python powinienem uzyc do [zadanie]?"
# Google - Zadaj pytanie "Jakiej paczki Python powinienem uzyc do [zadanie]?"
