from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def printarea(self):
        return self.length*self.breadth

r = rectangle(4,6)
print(r.printarea())

