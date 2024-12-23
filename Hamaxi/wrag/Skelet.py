import random
from Hamaxi.wrag.Enemy import Enemy


class Skelet(Enemy):
    def __init__(self,health):
        super().__init__(health)
    def takedamage(self,damage):
        ab = random.choice([1,2])
        if ab == 2:
            print("Скелет смог уклонится от удара героя")
        elif  ab == 1 :
            self.health -= damage
            print(" и наносит", damage, "урона и у противник остается", self.health, "сердечек")




