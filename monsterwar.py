from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."


class Axe(Weapon):
    def attack(self):
        return "Боец наносит удар топором."


# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "Боец без оружия!"

# Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        return f"{self.name} побежден!"

# Демонстрация боя
fighter = Fighter("Боец")
monster = Monster("Гоблин")

# Боец выбирает меч
fighter.change_weapon(Sword())
print(fighter.attack())
print(monster.defeat())

# Боец выбирает лук
fighter.change_weapon(Bow())
print(fighter.attack())
print(monster.defeat())


# Боец выбирает топор
fighter.change_weapon(Axe())
print(fighter.attack())
print(monster.defeat())
