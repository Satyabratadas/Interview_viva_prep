def fibo(n):
    a,b = 0,1
    for i in range(0,n):
        a,b = b,a+b
    return a
x = int(input())
for i in range(0,x):
    print(fibo(i))