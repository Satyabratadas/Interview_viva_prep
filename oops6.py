class A:
    classvar1 = "I am a class var in class A"
    def __init__(self):
        self.var = "I am a constructor in class A"
        self.classvar1 = "I am a instance var in class A"
        self.special = "Special"
    
class B(A):
    classvar1 = "I am a class var in class B"
    def __init__(self):
        super().__init__()
        self.var = "I am a constructor in class B"
        self.classvar1 = "I am a instance var in class B"
        

a = A()
b = B()
print(b.special,b.var,b.classvar1)