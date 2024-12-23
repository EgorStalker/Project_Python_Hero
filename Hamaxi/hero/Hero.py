from abc import ABC,abstractmethod
from Hamaxi.wrag.Enemy import Enemy
from Hamaxi.wrag.Mortal import Mortal

class Hero(ABC):
    def __init__(self,namehero,):
        self.namehero = namehero
        self.health = 100


    def get_namehero(self):
        return self.namehero

    @abstractmethod
    def attackEnemy(self,):
        pass

    def iSAlive(self):
        return self.health > 0
