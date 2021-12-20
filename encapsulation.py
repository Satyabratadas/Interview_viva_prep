class Base:
    def __init__(self):
        self.a = "Hello"
        self.__b = "World"

    

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Called Base Class")
        # print(self.__b)



o = Base()

print(o._Base__b)
