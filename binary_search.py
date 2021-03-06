def binary(arr,key):
    left = 0
    right = len(arr) - 1
    while(left<=right):
        mid = (left+right) //2
        if(arr[mid] == key):
            return mid
            
        elif(arr[mid]<key):
            left = mid+1
        else:
            right = mid-1
        
    return -1

if __name__ == '__main__':
    a = list(map(int,input().split()))
    a.sort()
    k = int(input())
    result = binary(a,k)
    if(result != -1):
        print('element found at',result)
    else:
        print('element not found')