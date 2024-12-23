from Hamaxi.wrag.Enemy import Enemy
import random

class Zombie(Enemy):
    def __init__(self,health):
        super().__init__(health)
    def takedamage(self, damage):
        ab3 = random.choice([1,2])
        self.health -= damage
        print("и он наносит", damage, "урона и у противника остается", self.health, "сердечек ")
        if ab3 == 1 and self.health == 0:
            print("Противник умер")
        elif ab3 == 2 and self.health == 0 :
            self.health +=100
            print("Противник воскрес у него здоровья ",self.health )