a = list(map(int,input().split()))
for i in range(len(a)):
    x = i
    for j in range(i+1,len(a)):
        if(a[x]>a[j]):
            x = j
    a[i],a[x] = a[x],a[i]

print('sorted array is\n')
for i in range(len(a)):
    print(a[i])