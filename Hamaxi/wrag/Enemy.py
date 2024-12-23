from Hamaxi.wrag.Mortal import Mortal


class Enemy(Mortal):
    def __init__(self,health):
        self.health = health

    def gethealth(self):
        return self.health

    def set_health(self,health):
        self.health = health

    def takedamage(self,damage):
        self.health -= damage
        print("и наносит",damage,"урона и у противника остается",self.health,"сердечек " )


    def attackHero(self, hero):
        if self.isAlive():  # Враг атакует, только если он жив
            damage = 10  # Урон, наносимый врагом
            print("///////")
            hero.takedamage(damage)


    def isAlive(self):
        if self.health > 0  and self.health <=100:
            return True
        else:
            return False


