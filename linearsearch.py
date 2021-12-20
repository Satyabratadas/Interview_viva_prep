def linear(arr,k):
    for i in range(len(arr)):
        if(arr[i] == k):
            return i
    return -1

a = list(map(int,input().split()))
a.sort()
key = int(input())
result = linear(a,key)
if(result != -1):
    print('found',result)
else:
    print('not found')
