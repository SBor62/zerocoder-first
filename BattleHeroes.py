import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Игрок атакует
            input("Нажмите Enter, чтобы атаковать...")
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен!")
                print(f"{self.player.name} победил!")
                break
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")

            # Компьютер атакует
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} повержен!")
                print(f"{self.computer.name} победил!")
                break
            print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    computer_name = "Компьютер"
    game = Game(player_name, computer_name)
    game.start()
