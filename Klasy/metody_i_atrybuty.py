#### Metody i atrybuty
### Atrybuty
## Atyrbuty instancji
class APICleint:
    def __init__(self, api_key, base_url):
        self.api_key = api_key  # Kazdy klient ma swoj wlasny klucz
        self.base_url = base_url  # Kazdy klient ma swoj wlasny URL
        self.request_count = 0  # Ilosc zapytan przez kazdego klienta


# Utworzenie instancji z nazwanymi argumentami
client1 = APICleint(api_key="key1", base_url="https://api1.com")
client2 = APICleint(api_key="key2", base_url="https://api2.com")


## Atrybuty instancji
class APIClient:
    version = "1.0"  # Takie samo dla kazdego klienta
    max_retries = 3  # Takie samo dla kazdego klienta

    def __init__(self, api_key):
        self.api_key = api_key  # Unikalne dla kazdego klienta


### Metody
class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid: {email}")
            return False
        return True

    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True

    def get_errors(self):
        return self.errors


# Uzycie walidatora
validator = DataValidator()

# Zauwaz: nie wpisujemy self, sam email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Lub uzywajac argumentow pozycyjnych
validator.validate_email("test@test.com")
validator.validate_age(150)

print(validator.get_errors())


## Przykład z filmiku
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("BARK!!!")


Aston = Dog("Aston")
Aston.name
Aston.bark()
