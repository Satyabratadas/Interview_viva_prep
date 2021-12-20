class Employee:
    def __init__(self,aname,asalary,arole):
        self.name =aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return(f"Name is {self.name},Salary is {self.salary},role is {self.role}")
    
    def __truediv__(self,other):
        return self.salary / other.salary

user1 = Employee('sam',500,'intrn')
user2 = Employee('Ram',255,'worker')
print(user1 / user2)

