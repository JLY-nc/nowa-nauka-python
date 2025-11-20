first_name = "Kuba"
last_name = "Down"

full_name = first_name + " " + last_name
print(full_name)

age = 25
message = "I am " + str(age) + " years old"
print(message)


imie = "Kuba"
wiek = 23
zawod = "Junior Automation Specialist"

print(f"Cześć, nazywam się {imie} i mam {wiek} lat.")
print(f"Pracuję jako {zawod}")

print("Cześć, nazywam się " + imie + " i mam " + str(wiek) + " lata")

# Skróty matematyczne
x = 10
x += 5
x *= 2
print(x)  # 30

# Powtórzenia
star = "*"
stars = star * 8
print(stars)  # ********

# Poprawianie tekstu
# Zmienianie wielkości liter
text = "Python Programming"

print(text.lower())  # python programming
print(text.upper())  # PYTHON PROGRAMMING
print(text.title())  # Python Programming

# Czysczenie tekstu
messy = "    hello world   "
print(messy.strip())  # "hello world" - usuwa białe pola

price = "$19.99"
print(price.strip("$"))  # "19.99" - usuwa ten znak, który chcemy usunąć

# Odnajdywanie w tekście oraz usuwanie
message = "I love Python programmin with Python"

# Sprawdzanie czy jakaś wartość istnieje
print("Python" in message)  # True
print(message.startswith("I"))  # True
print(message.endswith("Python"))  # True

# Odnajdywanie pozycji
print(message.find("Python"))  # 7 - na którym miejscu zaczyna się ta wartość
print(message.count("Python"))  # 2 - ilość wartości

# Zamiana wartości w tekście
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programmin with JavaScript"

# Pętle
# Powtórzenie tekstu
for i in range(5):
    print("Hello!")

# Python zaczyna liczyć od zera
for i in range(5):
    print(i)

# Pokazuje liczby od 1 do 5
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# Pokazuje co drugą liczbę od 0 do 10
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Pętle w tekście
name = "Python"
for letter in name:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n

# Pętla w listach
colors = ["red", "blue", "yellow"]
for color in colors:
    print(f"I like {color}")

# I like red
# I like blue
# I like yellow

# Pętle while
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# Count is 0
# Count is 1
# Count is 2
# Count is 3
# Count is 4

## Listy
fruits = ["apple", "banana", "orange"]  # Istotne aby był nawias kwadratowy []

# Wyciągnięcie określonej wartości w kolejności z listy
print(fruits[1])  # "banana" (druga wartość)
print(fruits[-1])  # "orange" (ostatnia wartość)
print(fruits[-2])  # "banana" (druga wartość od końca)

# Wycinanie fragmentów z list
print(fruits[0:2])  # ['apple', 'banana'] - tutaj pominięta została trzecia wartość
print(fruits[1:])  # ['banana', 'orange'] - tutaj pominięta została pierwsza wartość

# Zmienianie listy

# Podmiana wartości
fruits[0] = "papaya"
print(fruits)  # ['papaya', 'banana', 'orange'] - nastąpiła podmiana pierwszej wartości

# Dodawanie wartości
fruits.append("mango")  # dodaje na końcu wartość
fruits.insert(1, "strawberry")  # dodaje wartość na określonej pozycji
print(fruits)  # ['papaya', 'strawberry', 'banana', 'orange', 'mango']

# Usuwanie wartości
fruits.remove("banana")  # usuwa określoną wartość z listy
print(fruits)
last = fruits.pop()  # usuwa ostatnią wartość z listy
print(fruits)
del fruits[0]  # usuwa wartośc na określonym miejscu
print(fruits)

# Metody list
numbers = [3, 1, 2, 8, 7, 6]

# Informacyjne
print(len(numbers))  # mówi nam o długości listy
print(numbers.count(1))  # mówi nam o tym ile razy występuję dana wartość
print(
    numbers.index(8)
)  # mówi nam o tym na którym miejscu w liście znajduje się wartość

# Sortowanie
numbers.sort()
print(numbers)  # [1, 2, 3, 6, 7, 8]

numbers.reverse()
print(numbers)  # [8, 7, 6, 3, 2, 1]

# Kopiowanie
new_list = numbers.copy()

# Sprawdzanie listy
fruits = ["apple", "banana", "orange"]

# Sprawdzenie czy wartość znajduje się w liście
if "apple" in fruits:
    print("Found Apple!")

# Sprawdzenie czy lista jest pusta
if fruits:
    print("Has items!")
else:
    print("List is empty!")

## Słowniki
my_dict = {}  # Istotne, aby był ten nawias {}

# Słownik z danymi
person = {"name": "Alice", "age": 30, "city": "New York"}

# Inny sposób na tworzenie słownika
scores = dict(math=95, english=87, science=92)
print(scores)

# "Wyciąganie" danych ze słownika
# Wyciąganie danych poprzez klucz
print(person["name"])  # Alice
print(person["age"])  # 30

# Jest takze opcja z get()
print(person.get("city"))  # New York
print(person.get("job", "Unknown"))
# "Unknown" jest jako wartość domyślna w przypadku braku jakiejkolwiek wartości

# Wprowadzanie zmian w słowniku
person = {"name": "Alice", "age": 30, "city": "New York"}

# Dodawanie lub aktualizowanie
person["email"] = (
    "alice@email.com"  # Jezeli nie ma takiego klucza jak "email" to go doda do słownika
)
print(person)
person["age"] = (
    31  # Jezeli jest taki klucz jak "age" to obecna wartość ze słownika zostanie zaktualizowana
)
print(person)

# Usuwanie wartości
del person["email"]  # Usuwanie na podstawie klucza
print(person)
age = person.pop("age")  # Usunięcie i zwrócenie reszty wartości
print(person)
person.clear()  # Usuwa wszystkie wartości
print(person)


# Metody słowników
person = {"name": "Alice", "age": 30, "city": "New York"}

# Wyciągnięcie wszystkich klucz, wartości lub itemów
print(person.keys())  # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(
    person.items()
)  # dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# Sprawdzenie czy klucz istnieje
if "name" in person:
    print("Name found!")

# Aktualizacji wielu wartości
person.update({"age": 31, "job": "Engineer"})
print(person)

# Zagniezdzone słowniki
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 21, "grade": "B"},
    "Charlie": {"age": 19, "grade": "A"},
}

# Dostęp do zagniezdzonych danych
print(students["alice"]["grade"])  # "A"

## Tuple
# Róznia się tym od listy, ze raz ustalona wartosc nie moze zostac pozniej w zaden sposob zmodyfikowana - świetnie sprawdzi się przy koordynatach, kolorach RGB, konkretnych rekordach z bazy, wartościach zwracanych przez funkcje
# Pusty tuple
empty = ()  # Ten zbiór danych wyróznia klasyczny nawias ()

# Tuple z itemami
point = (3, 5)
colors = ("red", "green", "blue")

# Pojedynyczy item w tuple potrzebuje przecinka
single = (42,)  # to jest tuple
not_tuple = 42  # to jest zwykła liczba w nawiasach

# bez nawiasów (dorozumiany), czyli w domyśle mamy te wartości w nawiasie
coordiantes = 10, 20

# Dostęp do itemów
point = (3, 5)
colors = ("red", "green", "blue")

print(point[0])  # 3
print(colors[-2])  # green

# Wycinanie takze sie tutaj sprawdzi
print(colors[0:2])  # ('red', 'green')

# Rozpakowywanie tuple
point = (3, 5)
x, y = point  # x = 3, y = 5
print(y, x)

# Wielokrotne przypisanie
a, b, c = 1, 2, 3  # tak samo jak (1, 2, 3)
print(a)

# Zamiana wartości w zmiennych
x, y = y, x  # zamiana wartości
print(y)


## Zbiory - Set
# Zbiory mają unikalne wartości, kazdy element moze wystepowac tylko raz, a zatem są świetne do eliminacji duplikatów
# Wartości w zbiorach są nieuporządkowane, a co za tym idzie nie mozna ich wywolac po indeksie
# Niezmienność - o ile same zbiory są zmienne(mozna dodawac i usuwac wartosci), tak elementy w zbiorze muszą być niezmienne
# Mozna wykonywac szybkie operacje na zbiorach tj. sprawdzenie czy dana wartość nalezy do zbioru, łączenie zbiorow, przeciananie zbiorów lub wyodrębnienie róznic

# Pusty zbiór
empty_set = set()  # Musi być nawias (), poniewaz ten nawias {} odpowiada za słownik ale tylko w przypadku pustych zbiorów

# Przy ustalaniu wartości mozna to robić na obu nawiasach
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# Mozna utworzyc zbior z listy a on nam usunie duplikaty
scores = [85, 90, 90, 92, 85]
unique_scores = set(scores)
print(unique_scores)  # {90, 92, 85}

# Podstawowe operacje
colors = {"red", "blue"}

# Dodawanie elementów
colors.add("green")
print(colors)  # {'green', 'blue', 'red'}

# Usuwanie elementów
colors.remove("blue")  # ta operacja wywoła błąd jezeli nie znajdzie takiego elementu
colors.discard(
    "yellow"
)  # ta operacje nie wywoła błędu jezeli nie znajdzie takiego elementu

# Sprawdź członkostwo
if "red" in colors:
    print("Red is available")

# Najczęstsze zastosowanie
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(
    set(names)
)  # Ta konstrukcja pozwala napisać to krócej, a w rzeczywistosci oznacza unique_names = set(["Alice", "Bob", "Alice", "Charlie", "Bob"])
print(unique_names)

# Szybkie testowanie członkowstwa
allowed_users = {"alice", "bob", "charlie"}

if "alice" in allowed_users:
    print("Access granted")


# Funkcje
def greet():
    print("Hello, world!")
    print("Welcome to Python!")


greet()


# Składnia funkcji
def function_name():
    # Kod musi się znajdować po dwukropku pod funkcją
    # Kod, który nalezy do funkcji musi być wcięty
    pass


# Wywoływanie funkcji
# Aby wywołać funkcję, nalezy wpisac jej nazwe wraz z wraz z nawiasami
def say_goodbye():
    print("Goodbye!")
    print("See you later!")


say_goodbye()
say_goodbye()


# Funkcje wraz z zdaniami logicznymi
def check_weather():
    temperature = 25
    if temperature > 30:
        print("It is too hot!")
    else:
        print("Nice weather!")


check_weather()


# Zmienne posiadają zakres - gdzie dokładnie mogą być uzywane - rozrózniamy lokalne oraz globalne
# Lokalne zmienne
def caluculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total: {price + tax}")


caluculate_price()  # Total: 110.0

print(
    price
)  # ta funkcja nie zadziała poniewaz zmienna 'price' jest tylko i wylacznie w funkcji 'calculate_price' - nie jest to zmienna globalna

# Globalne zmienne
discount_rate = 0.5  # ta zmienna jest globalna poniewaz nie znajduje się bezpośrednio pod funkcja tylko jest ona napisana w samym pliku kodowym


def apply_discount(price):
    discount = price * discount_rate
    return price - discount


result = apply_discount(100)
print(result)

# Modyfikacja globalnych zmiennych
counter = 0  # Globalna zmienna


def increment():
    global counter  # Deklaracja o tym, ze chcemy zmodyfikowac globalną zmienną ## Unikać uzywania `global`, gdy to mozliwe. Utrudnia to poruszanie sie po kodzie - zrozumienie i debugowanie.
    counter += 1


increment()
increment()
print(counter)

# Zły przykład - uzywanie zmiennej globalnej
total = 0


def add_to_total(amount):
    global total
    total += amount


# Dobry przykład - uzywanie parametrow i funkcji return
def add_amounts(current_total, amount):
    return current_total + amount


total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total)


# Parametry
# Funkcja bez parametrów (nieelastyczna)
def greet_alice():
    print("Hello, Alice!")


# Funkcja z parametrami (elastyczna)
def greet(name):
    print(f"Hello, {name}")  # Hello, Alice!


greet("Alice")  # Hello, Alice
greet("Bob")  # Hello, Bob
greet("Charlie")  # Hello, Charlie


# Podstawowe parametry
def introduce(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old")


introduce("Kuba", 22)
introduce("Maria", 25)


# Wiele parametrów
def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")


# Kolejnosc ma znaczenie
calculate_total(100, 0.08, 10)


# Wartości domyślne
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


# Domyślna wartość
greet("Marek")  # Hello, Marek!

# Nadpisanie domyślnej wartości
greet("Bob", "Hi")  # Hi, Bob!
greet("Andrzej", "Siemano")  # Siemano, Andrzej!
# Wymagane parametry zawsze muszą być na początku, a te opcjonalne(czyli z domyślną wartością) na końcu


# Argumenty po słowach klucz
def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")


# Arugmenty ułozone na odpowiednich miejscach (kolejność ma znaczenie)
create_profile("Alicja", 22, "Wałbrzych")  # Alicja, 22, from Wałbrzych

# Argumenty uzupełnianie po słowie klucz (kolejność nie ma znaczenia)
create_profile(age=45, name="Tadek", city="Olsztyn")  # Tadek, 45, from Olsztyn
create_profile(city="Malbork", age=27, name="Mariusz")  # Mariusz, 27, from Malbork


# Return to
# Wyciąganie rezultatu z funkcji i zwrócenie jej do kodu, a nie drukowanie jej


# Ta funkcja tylko drukuje odpowiedz
def add_print(a, b):
    print(a + b)


# Ta funkcja zwraca wartość do kodu
def add_return(a, b):
    return a + b


# Teraz mozna uzyc rezultatu, który powstanie z funkcji 'add_return'
result = add_return(1, 2)
print(f"To jest Twój rezultat: {result}")  # To jest Twój rezultat: 3


# Uzycie return
def calculate_area(width, height):
    area = width * height
    return area


# Gdy Python dotrze do statementu `return` automatycznie wychodzi z funkcji, zaden kod po `return nie zadziała`

# Przechowanie zwróconej wartości
room_area = calculate_area(8, 18)
print(f"Room size: {room_area} sq ft")  # Room size: 144 sq ft


# Uzycie zwroconych wartosci
def double(number):
    return number * 2


# Przechowanie w zmiennej
result = double(5)  # 10

# Uzycie w wyrazeniach arytmetycznych
total = double(5) + double(2)  # 10 + 4 = 14

# Przekazanie do innej funkcji
print(double(3))  # 6

# Uzycie zwroconych wartosci w warunkach
if double(7) > 10:
    print("Big number!")  # Big number!


# Zwracanie wielu wartości
# Python moze zwrocic wiele wartosci jako tuple
def get_min_max(numbers):
    return min(numbers), max(
        numbers
    )  # To nam daje minimalna oraz maksymalna wartość z listy ponizej


# Zaciągnięcie dwóch wartości
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9


# Return vs print
def get_greeting_print(name):
    print(f"Hello, {name}!")  # Po prostu wyświetli rezultat


# Kod nie moze dalej w kodzie uzyc rezultatu, który został wydrukowany
message = get_greeting_print(
    "Alice"
)  # Wyświetla tekst ale zwraca wartość 'NONE' - Hello, Alice!
print(message)  # None


def get_greeting_return(name):
    return f"Hello, {name}!"  # Zwraca rezultat do kodu


# Kod moze uzyc tego rezultatu, który został zwrocony z powyzszej funkcji
message = get_greeting_return("Alice")  # Zwraca tekst
print(message.upper())
