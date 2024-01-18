import threading
import time
import random

class Unit:
    def __init__(self, name, currency_per_second, health):
        self.name = name
        self.currency_per_second = currency_per_second
        self.health = health
        self.is_alive = True

    def generate_currency(self):
        while self.is_alive:
            time.sleep(1)
            currency = self.currency_per_second
            print(f"{self.name} заробив {currency} грошей")

    def attack(self, enemy):
        while enemy.is_alive and self.is_alive:
            time.sleep(2)
            damage = random.randint(1, 5)
            enemy.health -= damage
            print(f"{self.name} наніс {damage} шкоди {enemy.name}. Залишено здоров'я {enemy.name}: {enemy.health}")
            if enemy.health <= 0:
                enemy.is_alive = False
                print(f"{enemy.name} був знищений!")

class Game:
    def __init__(self):
        self.player = Unit("Гравець", 5, 20)
        self.enemy = Unit("Ворог", 3, 15)

        self.player_thread = threading.Thread(target=self.player.generate_currency)
        self.enemy_thread = threading.Thread(target=self.enemy.generate_currency)

        self.attack_thread = threading.Thread(target=self.player.attack, args=(self.enemy,))
        self.defense_thread = threading.Thread(target=self.enemy.attack, args=(self.player,))

    def start(self):
        self.player_thread.start()
        self.enemy_thread.start()
        self.attack_thread.start()
        self.defense_thread.start()

        # Чекаємо, доки гравець або ворог не втратять життя
        while self.player.is_alive and self.enemy.is_alive:
            user_input = input("Натисніть 'a' для атаки: ")
            if user_input.lower() == 'a':
                self.player.attack(self.enemy)

        # Завершуємо гру, якщо хтось втратив життя
        self.player_thread.join()
        self.enemy_thread.join()
        self.attack_thread.join()
        self.defense_thread.join()

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()