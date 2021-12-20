a = list(map(int,input().split()))
k = int(input())
a.sort()
for i in a:
    if (a[i] == k):
        x = a[i]
        break
print(x)
