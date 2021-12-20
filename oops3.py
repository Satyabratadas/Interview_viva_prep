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


user1 = Employee('sam',500,'intrn')


# print(user1.salary) 
# print(user2.print_details())
user1.change_leaves(20)
print(user1.no_of_leavs)

