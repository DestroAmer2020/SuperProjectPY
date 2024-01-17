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

def main():
    player = Unit("Гравець", 5, 20)
    enemy = Unit("Ворог", 3, 15)

    player_thread = threading.Thread(target=player.generate_currency)
    enemy_thread = threading.Thread(target=enemy.generate_currency)

    attack_thread = threading.Thread(target=player.attack, args=(enemy,))
    defense_thread = threading.Thread(target=enemy.attack, args=(player,))

    player_thread.start()
    enemy_thread.start()
    attack_thread.start()
    defense_thread.start()

    player_thread.join()
    enemy_thread.join()
    attack_thread.join()
    defense_thread.join()

if __name__ == "__main__":
    main()