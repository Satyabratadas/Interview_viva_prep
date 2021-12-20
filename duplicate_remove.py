string = input()
lst = []
for i in string:
    if i  not in lst:
        lst.append(i)
s = ''.join(lst)
print(s)