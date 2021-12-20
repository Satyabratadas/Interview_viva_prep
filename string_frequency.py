st = input()
st1 = {}
for i in st:
    if i in st1:
        st1[i] += 1
    else:
        st1[i] = 1
print((st1))
    