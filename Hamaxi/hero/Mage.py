from Hamaxi.hero.Hero import Hero
from Hamaxi.wrag.Enemy import Enemy
class Mage(Hero):
    def __init__(self,namehero):
        super().__init__(namehero)

    def attackEnemy(self,enemy):
        damage = 25
        print(self.namehero, " быстро кидает електричиский заряд  на врага и")
        enemy.takedamage(damage)
        if self.health == 0:
            print(self.namehero, "умер ")
    def health_mage(self):
        self.health +=25