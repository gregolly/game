# Character: mother class
# Hero: Controlled by user
# Enemy: User enemy
from random import randint

class Character:
    def __init__(self, name, health, level) -> None:
        self.__name = name
        self.__health = health
        self.__level = level

    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    
    def get_level(self):
        return self.__level
    
    def show_details(self):
        return f"Name: {self.get_name()}\nHealth: {self.get_health()}\nLevel: {self.get_level()}"
    
    def receive_damage(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            self.__health = 0

    def strike(self, target):
        damage = randint(self.__level * 2, self.__level * 4)
        target.receive_damage(damage)
        print(f"{self.get_name()} striked {target.get_name()} and caused {damage} of damage!")
    
    
    
class Hero(Character):
    def __init__(self, name, health, level, skill) -> None:
        super().__init__(name, health, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill
    
    def show_details(self):
        return f"{super().show_details()}\nSkill: {self.get_skill()}"
    
    def especial_strike(self, target):
        damage = randint(self.__level * 5, self.__level * 8)
        target.receive_damage(damage)
        print(f"{self.get_name()} used a especial strike on {target.get_name()} and caused {damage} of damage!")
    
class Enemy(Character):
    def __init__(self, name, health, level, type) -> None:
        super().__init__(name, health, level)
        self.__type = type

    def get_type(self):
        return self.__type
    
    def show_details(self):
        return f"{super().show_details()}\nType: {self.get_type()}"
    
class Game:
    """Class created to management the game"""
    def __init__(self) -> None:
        self.hero = Hero(name="Joaquim Hero", health=100, level=5, skill="Unhuman strong")
        self.enemy = Enemy(name="Rafael Enemy", health=100, level=5, type="Zombie")

    def start_battle(self):
        """Management the battle turns"""
        print("Starting battle!")
        while self.hero.get_health() > 0 and self.enemy.get_health() > 0:
            print("\nCharacters Details:")
            print(self.hero.show_details(), "\n")
            print(self.enemy.show_details(), "\n")

            input("Press Enter to strike...")
            select = input("Select (1 - Normal strike, 2 - Especial Strike): ")

            if select == "1":
                self.hero.strike(self.enemy)
            else:
                print("Invalid select. Select one of the two options!")

            if select == "2":
                self.hero.especial_strike(self.enemy)
            else:
                print("Invalid select. Select one of the two options!")

            if self.enemy.get_health() > 0:
                self.enemy.strike(self.hero)

        if self.hero.get_health() > 0:
            print(f"The battle has been ended, {self.hero.get_name()} won the battle!")
        else:
            print(f"The battle has been ended, {self.enemy.get_name()} won the battle!")



game = Game()
game.start_battle()

