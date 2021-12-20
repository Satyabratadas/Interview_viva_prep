class Employee:
    var = 9
    _var2 = 10
    __var3 = 11
    def __init__(self,aname,asalary,arole):
        self.name =aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return(f"Name is {self.name},Salary is {self.salary},role is {self.role}")
# print('Enter the details of first user')
# x = input()
# y = int(input())
# z = input()
user1 = Employee('sam',500,'intrn')
# print('Enter the details of second user')
# p = input()
# q = int(input())
# r = input()
# user2 = Employee(p,q,r)

print(user1._Employee__var3) 