import random

class Player:
    def __init__(
            self, 
            name:str, 
            max_health:int, 
            money:int,
            min_damage:int,
            max_damage:int):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.money = money
        self.has_weighted_rock = False
        self.has_paper_armor = False
        self.has_sharpened_scissors = False
        self.has_crown = False

    def take_damage(self, dmg:int):
        self.health -= dmg

    def refill_health(self):
        self.health = self.max_health

    def pay_gold(self, price:int):
        self.money -= price

    def update_min_dmg(self, bonus:int):
        self.min_damage += bonus

    def update_max_dmg(self, bonus:int):
        self.max_damage += bonus

    def update_max_health(self, bonus:int):
        self.max_health += bonus


class Enemy:
    def __init__(
            self, 
            name:str, 
            health:int,
            min_damage:int,
            max_damage:int):
        self.name = name
        self.health = health
        self.min_damage = min_damage
        self.max_damage = max_damage

    def rps_choice(self):
        return random.randint(1,3)
    
    def take_damage(self, dmg:int):
        self.health -= dmg
