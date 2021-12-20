st = input()
lst = []
for i in st:
    if st.count(i)>1:
        if i not in lst:
            lst.append(i)
s = ''.join(lst)
print(s)