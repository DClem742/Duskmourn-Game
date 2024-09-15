import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.health_potions = 0 

    def display_inventory(self):
            print(f"\n{self.name}'s Inventory:")
            print(f"Health Potions: {self.health_potions}")
            print(f"Current Health: {self.health}/{self.max_health}")

    def add_health_potions(self, amount):
        self.health_potions += amount
        print(f"You received {amount} health potion(s). Total: {self.health_potions}")

    def use_health_potion(self):
        if self.health_potions > 0:
            heal_amount = min(50, self.max_health - self.health)
            self.health += heal_amount
            self.health_potions -= 1
            print(f"You used a health potion and restored {heal_amount} HP!")
        else:
            print("You don't have any health potions!")

    def take_damage(self, damage):
        if self.shield_active:
            damage = damage // 2
        self.health -= max(damage - self.defense, 0)
class Hero(Character):
    def __init__(self, name, health, attack, defense, special_ability):
        super().__init__(name, health, attack, defense)
        self.special_ability = special_ability
        self.special_cooldown = 0

class Sean(Hero):
    def __init__(self):
        super().__init__("Sean", 100, 15, 10, "Tech-hack")

    def tech_hack(self, enemies):
        for enemy in enemies:
            enemy.stunned = True
        return "Sean hacks technology around him, stunning nearby enemies!"

class Pat(Hero):
    def __init__(self):
        super().__init__("Pat", 80, 20, 5, "Shout")

    def shout(self):
        self.attack = self.base_attack * 2
        return "Pat yells at the enemy, doubling his attack power!"

class TheMeg(Hero):
    def __init__(self):
        super().__init__("The Meg", 90, 12, 8, "Shield")

    def shield(self):
        self.shield_active = True
        return "The Meg casts a protective barrier, halving incoming damage!"

class Enemy(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
        self.stunned = False


    