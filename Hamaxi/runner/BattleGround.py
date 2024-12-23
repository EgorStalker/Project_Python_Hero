from Hamaxi.hero.Hero import Hero
from Hamaxi.hero.Warrior import Warrior, enemy, skelet1
from Hamaxi.hero.Mage import Mage
from Hamaxi.hero.Archer import Archer
from Hamaxi.wrag import Enemy
from Hamaxi.wrag.Skelet import Skelet
from Hamaxi.wrag.Zombie import Zombie
skelet12 = Skelet(100)
zombie3000= Zombie(100)
warrior1 = Warrior("Алекса")
archer1 = Archer("Каха")
mage1 = Mage("Ара")
# print(warrior1.attackEnemy(enemy))
print(warrior1.attackEnemy(skelet1))

print(archer1.attackEnemy(zombie3000))
print(mage1.attackEnemy(zombie3000))
