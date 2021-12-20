class Employee:
    no_of_leavs = 20
    def __init__(self,fname,lname):
        self.firstname =fname
        self.lastname = lname
    @property
    def email(self):
        if self.firstname == None or self.lastname == None:
            return('Email is not set , please give the name')
        else:
            return(f"{self.firstname}.{self.lastname}@gmail.com")
    
    @email.setter
    def email(self,string):
        print('Setting now.....')
        names = string.split('@')[0]
        self.firstname = names.split('.')[0]
        self.lastname = names.split('.')[1]
    @email.deleter
    def email(self):
        self.firstname = None
        self.lastname = None


    # def print_details(self):
    #     return(f"Name is {self.name},Salary is {self.salary},role is {self.role}")
    # @classmethod
    # def change_leaves(cls,leaves):
    #     cls.no_of_leavs = leaves


user1 = Employee('Sam','intrn')
print(user1.email)
user1.firstname = 'Ram'
print(user1.email)
user1.email = 'Nil.das@gmail.com'
print(user1.firstname)
print(user1.lastname)
del user1.email
print(user1.email)



# print(user1.salary) 
# print(user2.print_details())

