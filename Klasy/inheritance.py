# #### Dziedziczenie (Inheritance)
# # Klasa Parent - ogólne zwierze
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         return f"{self.name} is eating"

#     def sleep(self):
#         return f"{self.name} is sleeping"


# # Klasa Child - szczególne zwierze
# class Dog(Animal):
#     def bark(self):
#         return f"{self.name} says woof!"


# # Utworzenie psa poprzez argument pozycyjny
# my_dog = Dog("Buddy")
# # Lub poprzez argument nazewnictwa
# my_dog2 = Dog(name="Max")

# # Pies moze robić czynności jak zwierze (odziedziczone)
# print(my_dog.eat())  # Buddy is eating
# print(my_dog.sleep())  # Buddy is sleeping

# # Ale pies tez moze robic czynnosci jak pies
# print(my_dog.bark())  # Buddy says woof!

## Dodawanie atrybutów do klasy child
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_pet = True


# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  # Przekazanie imienia do klasy parent `__init__`
#         # `super().__init__()` wywołuje metodę `__init__` z klasy parent. Dzięki temu klasa nadrzędna prawidłowo konfiguruje swoje atrybuty, zanim klasa podrzędna doda swoje własne.
#         self.breed = breed  # Atrybuty tylko dla psa

#     def describe(self):
#         return f"{self.name} is a {self.breed}"


# # Utworzenie psa wraz z ich rasą poprzez argument pozycyjny
# golden = Dog("Buddy", "Golden Retriever")

# # Lub poprzez argument nazewnictwa (bardziej przejrzyste)
# poodle = Dog(name="Max", breed="Poodle")

# print(golden.describe())  # Buddy is a Golden Retriever
# print(golden.is_pet)  # True (inherited from Animal)

## Nadpisywanie metod - podrzędna klasa moze zmienic działanie metody klasy nadrzędnej
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         return f"{self.name} makes a sound"

# class Dog(Animal):
#     def make_sound(self):  # Nadpisanie metody z klasy nadrzędnej
#         return f"{self.name} barks: Woof!"

# class Cat(Animal):
#     def make_sound(self):  # Nadpisanie metody z klasy nadrzędnej
#         return f"{self.name} meows: Meow!"

# # Rózne zwierzęta wydają rozne dźwięki
# generic = Animal(name="Something")
# dog = Dog(name="Buddy")
# cat = Cat(name="Whiskers")

# print(generic.make_sound())  # Something makes a sound
# print(dog.make_sound())      # Buddy barks: Woof!
# print(cat.make_sound())      # Whiskers meows: Meow!

## Realny przykład
class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False

    def load(self):
        print(f"Loading {self.model_name}...")
        self.is_loaded = True


class TextModel(BaseModel):
    def __init__(self, model_name, max_length=1000):
        super().__init__(model_name)
        self.max_length = max_length

    def process_text(self, text):
        if not self.is_loaded:
            self.load()
        # W razie potrzeby skróćŔ
        if len(text) > self.max_length:
            text = text[: self.max_length]
        return f"Processed: {text}"


# Uzyj model z nazwanymi argumentami
model = TextModel(model_name="gpt-3.5-turbo", max_length=100)

# Wywolaj metode - nie potrzeba parametru `self`
result = model.process_text(text="Hello world")
print(result)  # Loading gpt-3.5-turbo...
# Processed: Hello world
