class Employee:
    no_of_leaves = 8
    pass

ram = Employee()
sam = Employee()

ram.name = 'Ram'
ram.salary = 9000

sam.name = 'sam'
sam.salary = 8000

print(ram.name)
print(ram.salary)
print(Employee.no_of_leaves)
sam.no_of_leaves = 10
print(Employee.no_of_leaves)
print(sam.__dict__)
