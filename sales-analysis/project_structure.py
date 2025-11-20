# import os

# # Sprawdzenie czy znajdujemy się we właściwym folderze oraz pliku
# print(
#     "Current directory:", os.getcwd()
# )  # os.getcwd() pozwala na sprawdzenie, gdze obecnie w srodowisku wirtualnym pracujemy

# # Sprawdzenie czy plik z danymi `sales.csv` istnieje
# data_path = "data/sales.csv"  # Jezeli chcialbym iść do folderu wyzej musiałbym zapisać `../data/paris_weather.csv`, najwazniesjze jest ta notacja `../`
# if os.path.exists(data_path):
#     print(f"Found {data_path}")
# else:
#     print(f"Cannot find {data_path}")
#     print("Make sure you're running the sales-analysis folder!")

# ## Przykłady poruszania się po folderach
# # "data/sales.csv" schodzimy do folderu nizej
# # "../config.json" idziemy o jeden poziom wyzej do pliku/folderu
# # "helper.py" sprawdzamy w tym samym folderze

# # Dla importu:
# import helper  # Ten sam folder - nie potrzeba zadnej sciezki
# import data.processor  # Schodzimy do folderu nizej(data) do pliku o nazwie processor

# # Import nadrzędnych folderów wymaga `sys.path`:
# import sys

# sys.path.append("...")  # Dodanie nadrzędnego folderu do sciezki
# import parent_module  # Teraz mozna zaimportowac plik z folderu wyzej


# # Pliki vs moduły
# # Python obsługuje klasyczne pliki oraz moduły Python w rózny sposob


# # Klasyczne pliki
# # Odczytanie pliku csv - wymaga dokladnej sciezki
# with open("data/sales.csv", "r") as file:
#     content = file.read()
#     print(content)

# # Moduły Python
# # Python przeszukuje rózne sciezki (sys.path)
# # Importowanie modułu - Python będzie go szukał
# import mymodule  # Szuka pliku mymodule.py
# from folder.utils import helper  # Szuka folderu folder/utils.py

# # Jak Python znajduje moduły
# # Python szuka modułów (czyli innych plików .py) w roznych miejscach, mozna sprawdzic te miejsca za pomocą
# import sys

# print(sys.path)  # Lista folderów sprawdzonych przez Python

# ## Co zawiera lista:
# # 1. Folder, który zawiera skrypt
# # 2. Foldery z wbudowaną biblioteką Pythona
# # 3. Zainstalowane paczki

# ## Dodawanie własnych folderów
# import sys

# # Dodanie folderu do sciezki przeszukiwanej przez Python
# sys.path.append("/path/to/my/folder")

# # Teraz mozna zaimportowac plik z tego folderu
# import mymodule

# # Klasyczny przyklad importu z "wyzszego folderu"
# import sys
# import os

# # Teraz trzeba pojsc poziom wyzej, niz gdzie sie znajduje obecny skrypt
# parent = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(parent)

# # Model mentalny dla tego działania: Znaj folder w którym się znajdujesz, znaj miejsce docelowe do którego chcesz się dostać, nawiguj poprzez znak `/` jezeli chcesz się dostać do pliku. Dla importu w tym samym folderze nie potrzebujesz `/`, podfoldery wywołasz poprzez `.`, a foldery wyzej poprzez sys.path

