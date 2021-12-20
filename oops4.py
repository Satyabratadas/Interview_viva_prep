class Employee:
    no_of_leavs = 20
    def __init__(self,aname,asalary,arole):
        self.name =aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return(f"Name is {self.name},Salary is {self.salary},role is {self.role}")
    @classmethod
    def change_leaves(cls,leaves):
        cls.no_of_leavs = leaves
    
    @classmethod
    def from_string(cls,string):
        return cls(*string.split("-"))
    
    @staticmethod
    def print_things():
        return("Ale , Bhendi , Gajar")


user1 = Employee("sam",500,"emp")      #from_string("sam-500-coder")


# print(user1.salary) 
# print(user2.print_details())
user1.change_leaves(22)
print(user1.no_of_leavs)
# print(user1.name)
# print(user1.print_things())


