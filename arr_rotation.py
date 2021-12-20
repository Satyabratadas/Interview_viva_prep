n = int(input("How many rotation can you do \n"))
a = list(map(int,input().split()))
x = input()
if(x == 'r' ):
    a = a[-n:]+a[:-n]    #right shift
elif(x == 'l'):
    a = a[n:]+a[:n]    #left shift

print(a)