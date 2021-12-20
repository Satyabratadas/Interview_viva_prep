class B:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return self.a+other.a
ob1 = B(2)
ob2 = B(4)
ob3 = B("Hello")
ob4 = B("World")

print(ob1+ob2)
print(ob3+ob4)
