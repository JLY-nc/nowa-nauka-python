# Syntax Error - pojawia się gdy Python nie jest w stanie zrouzmieć kodu
if x > 5
    print("Big number")

# Naprawiona wersja
x = 4
if x > 5:
    print("Big number")

# Błąd podczas egzeukcji kodu
# Dzielenie przez zero
result = 10/0 # ZeroDivisionError

# Zmienna nie istnieje
print(score) # NameError

# Zły typ wartości
"hello" + 5 # TypeError

# Dlaczego obsługiwać błędy
# Ten fragment kodu nie zadziała, jezeli nie znajdzie tego pliku
with open('data.txt', 'r') as f:
    content = f.read()
print("Done!") # Jezeli brakuje pliku to kod nigdy tutaj nie dotrze

# Tutaj jest kod, który niezaleznie od tego czy pilk jest czy go nie ma to zadziała
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Could not find data.txt")
    content = "default data"
print("Done!") # Zawsze kod dotrze do tego miejsca

# Podstawowa struktura Try i except
# Blok `try` zawiera kod, który moze sie "popsuć"
# Blok `except` zostaje odpalony jak błąd wystąpi
try:
    # Kod, który moze się popsuć
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    # Kod który jest uruchamiany, gdy błąd wystąpi
    print("Could not find data.txt")
    content = "default data"
print("Done!")

# Wyłapywanie specyficznych błędów
try:
    age = int(input("Wprowadź swój wiek: "))
    print(f"Za 10 lat będziesz miał {age + 10} lata")
except ValueError:
    print("Please enter a number")

# Obsługa wielu rodzajów błędów
try:
    # Przeczytaj numer z pliku
    with open('number.txt', 'r') as f:
        text = f.read()
    number = int(text)
    result = 100 / number
    print(f"Result: {result}")
except FileNotFoundError:
    print("Could not find number.txt")
except ValueError:
    print("File doesn't contain a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Klauzla `else`
# Uzycie tej klauzli w try i except zostanie uruchomiony tylko jeśli nie wystąpi zaden błąd
try:
    with open('data.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
else:
    # Ten kod uruchomi się tylko jezeli ten plik zostanie poprawnie otwarty
    print(f"File has {len(data)} characters")

# Klauzla `finally`
# Ta klaula zawsze się uruchamia nie wazne czy wystąpi błąd czy nie
try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # Ten kod zawsze sie uruchomi, aby poczyścić to co się przetworzyło
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup complete")


### FileNotFoundError
# Ten kod pokaze błąd jezeli plik nie istnieje
with open('missing.txt', 'r') as f:
    content = f.read()

## Fix
import os
if os.path.exists('data.txt'):
    with open('data.txt', 'r') as f:
        content = f.read()

else:
    print("File not found")

# Lub mozna uzyc metody try-except
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    content = "" # Domyślna wartość

### ValueError
# To powoduje błędy:
int("hello") # Nie moze przekształcić tej wartości w liczbę
int("12.5") # int() nie przetwarza kropek
list.remove("x") # element nie znajduje się na liście

## Fix
# Zwalidować input uzytkownika
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a number")

# Przkształcaj ostroznie
float_str = "12.5"
number = int(float(float_str)) # Przekształć do float najpierw
print(number)

### Key Error
user = {"name": "Alice", "age": 25}
print(user["email"]) # KeyError - brak klucza "email"

## Fix
# Sprawdź czy klucz istnieje
if "email" in user:
    print(user["email"])

# Uzycie get() z wartością domyślną
email = user.get("email", "no-email@example.com")

# Lub nalezy wprowadzic obsługę błędu
try:
    print(user["email"])
except KeyError:
    print("Email not found")

### IndexError
numbers = [1, 2, 3]
print(numbers[5]) # IndexError - są tylko 3 elementy na liście, a my chcemy wywołać element numer 6

## Fix
# Sprawdź w pierwszej kolejności długość
if len(numbers) > 5:
    print(numbers[5])

# Uzycie negacji w indeksowaniu ostroznie
last_item = numbers[-1] if numbers else None

# Obsługa błędu
try:
    print(numbers[5])
except IndexError:
    print("List is too short")

### TypeError
# To wywołuje błędy
"hello" + 5 # Nie mozna dodac liczby do tekstu
len(42) # Liczby nie mają długości
int([1, 2, 3]) # Nie mozna przeksztalcic listy do liczby

## Fix
# Wyraźne konwertowanie typów
"hello" + str(5) # "hello5"
str(42) # "42"

# Zweryfikuj najpierw typ
if isinstance(value, str):
    print(len(value))

### AttributeError
text = "hello"
text.append("!") # AttributeError - ciągi znaków nie posiadają atrybutu `append`

## Fix
# Uzywaj poprawnych metod
text = "hello"
text = text + "!" # Ciągi znaków są niezmienne

# Sprawdź czy atrybut istnieje
if hasattr(obj, 'append'):
    obj.append