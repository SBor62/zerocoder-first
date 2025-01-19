class Animal():    #
    def __init__(self, name, age):  #
        self.name = name
        self.age = age
    def eat(self):   #
        print(f"{self.name} ест")
    def make_sound(self):   #
        pass

class Bird(Animal):    #
    def make_sound(self):
        print("кря кря")


class Mammal(Animal):    #
    def make_sound(self):
        print("гав")


class Reptile(Animal):    #
    def make_sound(self):
        print("шшш-ссс")

def animal_sound(animals):    #
    for animal in animals:
        animal.make_sound()


class Zoo():   #
    def __init__(self):  #
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f"Сотрудник {new_staff} добавлен в персонал зоопарка")


class ZooKeeper():   #
    def feed_animal(self, animal):
        print(f"Сотпудник кормит {animal.name}")



class Veterinarian():   #
    def heal_animal(self, animal):
        print(f"Ветеринар лечит {animal.name}")

#
bird1 = Bird(name="Утка", age= 1)
mammal1 = Mammal(name= "Собака", age= 3)
reptile1 = Reptile(name= "Удав", age= 5)

#
zoo = Zoo()

#
keeper = ZooKeeper()
veterinarian = Veterinarian()

#
zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zoo.add_staff(keeper)
zoo.add_staff(veterinarian)

#
animal_sound(zoo.animals)

#
keeper.feed_animal(mammal1)
veterinarian.heal_animal(bird1)
