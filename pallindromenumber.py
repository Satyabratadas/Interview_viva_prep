
def pallindrome(n):
    # z = str(n)
    if(n == n[::-1]):
        print('pallindrome')
    else:
        print('not pallindrome')


x = input()
pallindrome(x)