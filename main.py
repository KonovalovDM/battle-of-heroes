import pygame

# Создаем класс Hero
class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Атакует другого героя, уменьшая его здоровье."""
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} единиц урона здоровью игрока.")
        other.health -= self.attack_power

    def is_alive(self):
        """Проверяет, жив ли герой."""
        return self.health > 0

# Создаем класс Game
class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        """Запускает игровой процесс."""
        print("Начало игры!")

        while self.player.is_alive() and self.computer.is_alive():
            # Игрок атакует компьютер
            self.player.attack(self.computer)
            self.display_status()

            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break

            # Компьютер атакует игрока
            self.computer.attack(self.player)
            self.display_status()

            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break

    def display_status(self):
        """Отображает текущий статус здоровья героев."""
        print(f"{self.player.name}: {self.player.health} жизненных сил, {self.computer.name}: {self.computer.health} жизненных сил\n")

# Реализация игрового цикла
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()