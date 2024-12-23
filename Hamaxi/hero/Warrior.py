from Hamaxi.hero.Hero import Hero
from Hamaxi.wrag.Enemy import Enemy
import random

from Hamaxi.wrag.Skelet import Skelet


class Warrior(Hero):
    def __init__(self,namehero):
        super().__init__(namehero,)

    def attackEnemy(self,enemy,):
        ab1 = random.choice([1,2])
        damage = 30
        if ab1 ==  1 :
            print(self.namehero, " быстро кидает накидуется  на врага своим мечем  и")
            enemy.takedamage(damage )
        elif ab1 == 2 :
            damage  = 60
            print(self.namehero, " быстро кидает накидуется  на врага своим увеличеным магическим мечем и")
            enemy.takedamage(damage)
        elif self.health == 0:
            print(self.namehero, "умер ")


enemy = Enemy(100)
skelet1 = Skelet(100)
