str = input('enter the main string \n')
x = input('enter the character which want to count \n')
count = 0
for i in str:
    if (i == x):
        count += 1
print(f"Count of {x} in the given string is {count} ")