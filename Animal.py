class Animal():    # Создание класса Животные
    def __init__(self, name, age):  # Общие характеристики животных
        self.name = name
        self.age = age

    def eat(self):    # Общие функции животных
        print(f"{self.name} ест")

    def make_sound(self):
        pass


class Bird(Animal):    # Создание производного класса птиц
    def make_sound(self):
        print("кря кря")


class Mammal(Animal):    # Создание производного класса млекопитающих
    def make_sound(self):
        print("гав")


class Reptile(Animal):    # Создание производного класса рептилий
    def make_sound(self):
        print("шшш-ссс")


def animal_sound(animals):    # демонстрация полиморфизма - одна функция для всех животных
    for animal in animals:
        animal.make_sound()


class Zoo():   # Создание независимого класса Зоопарк
    def __init__(self):  # Создание списков животных и сотрудников
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f"Сотрудник {new_staff} добавлен в персонал зоопарка")


class ZooKeeper():   # Содание класса сотрудников
    def feed_animal(self, animal):
        print(f"Сотпудник кормит {animal.name}")


class Veterinarian():   # Создание класса ветеринаров
    def heal_animal(self, animal):
        print(f"Ветеринар лечит {animal.name}")

# Создание объектов классов животных
bird1 = Bird(name="Утка", age= 1)
mammal1 = Mammal(name= "Собака", age= 3)
reptile1 = Reptile(name= "Удав", age= 5)

# Создание объекта Зоопарк
zoo = Zoo()

# Создание объектов сотрудников
keeper = ZooKeeper()
veterinarian = Veterinarian()

# Добавление животных и сотрудников в зоопарк
zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zoo.add_staff(keeper)
zoo.add_staff(veterinarian)

# Вызов функции animal_sound для всех животных зоопарка
animal_sound(zoo.animals)

# Вызов функций для сотрудников зоопарка
keeper.feed_animal(mammal1)
veterinarian.heal_animal(bird1)