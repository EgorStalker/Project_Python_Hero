from abc import ABC,abstractmethod
class Mortal(ABC):
    @abstractmethod
    def isAlive(self):
        pass