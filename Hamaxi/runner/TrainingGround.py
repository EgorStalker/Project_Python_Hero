from Hamaxi.hero.Hero import Hero
from Hamaxi.hero.Warrior import Warrior,enemy
from Hamaxi.hero.Mage import Mage
from Hamaxi.hero.Archer import Archer
from Hamaxi.wrag import Enemy

Warrior1 = Warrior("Алекса")
Mage1 = Mage("Акаме")
Archer1 = Archer("Мисаката")
# print(Warrior1.attackEnemy(enemy), Mage1.attackEnemy(), Archer1.attackEnemy())
print(Warrior1.attackEnemy(enemy))
print(Mage1.attackEnemy(enemy))

