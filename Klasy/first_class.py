### Podstawowa struktura klasy
# Kazda klasa zaczyna się od słowa klucz `class`


# class Dog:  # Zauwaz, ze kazda nazwa klasy uzywa PascalCase - czyli jest pisana w taki sposób 'MyDogIsBeautiful'
#    pass  # Pusta klasa

### Dodawanie inicjalizatora
# Metoda `__init__` działa w momencie, gdy tworzymy nowy obiekt
# class Dog:
# def __init__(self, name, breed):
#     self.name = name
#     self.breed = breed


# Utwórz obiekty psa - uzywajac argumentów pozycjonowanych
# dog1 = Dog("Aston", "Doberman")
# dog2 = Dog("Martin", "Rottweieler")

# # Lub uzywajac argumentow nazwanych (bardziej przejrzyscie)
# dog3 = Dog(name="Banjo", breed="Husky")

# print(dog1.name)
# print(dog2.breed)

### Zrozumienie self
class Dog:
    def __init__(self, name):
        self.name = name  # self.name jest przypisany do konkretnego psa


# Uzywanie argumentow pozycyjnych
dog1 = Dog("Aston")

# Uzywanie argumentów nazwanych (ten sam rezultat)
dog2 = Dog(name="Martin")

# Kazdy pies ma swoje własne imię
print(dog1.name)  # Aston
print(dog2.name)  # Martin


## Przykład realnego zastosowania
class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"


# Utworzenie róznych konfiguracji
# Uzywanie pozycyjnych do wymaganych argumentów oraz nazwanych dla opcjonalnych
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Uzycie wszystkich nazwanych argumentow (najbardziej przejrzysty)
prod_config = APIConfig(api_key="sk-dev-key", model="gpt-5", max_tokens=1000)

# Dostęp do konfiguracji
print(dev_config.model)
print(prod_config.max_tokens)
print(prod_config.api_key)

## Klasy vs instancje
# APIConfig jest klasą
# dev_config oraz prod_config są instancjami
# Kazda instancja ma swoje własne dane
# Zmiana w jednej instancji nie wpływa na drugą
