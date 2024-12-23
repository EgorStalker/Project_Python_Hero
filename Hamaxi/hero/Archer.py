from Hamaxi.hero.Hero import Hero
from Hamaxi.hero.Warrior import enemy


class Archer(Hero):
    def __init__(self,namehero):
        super().__init__(namehero)

    def attackEnemy(self,enemy):
        damage = 15
        print(self.namehero, " быстро достаёт свой лук и выпускает две стрелы по по врагу и  ")
        enemy.takedamage(damage)
        print(self.namehero, "выпускает вторую стрелу по врагу")
        enemy.takedamage(damage)
        if self.health == 0:
            print(self.namehero, "умер ")