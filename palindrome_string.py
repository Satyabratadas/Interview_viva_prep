def ispalindrome(s):
    if (s == s[::-1]):
        print("Yes!it's pallindrome")
    else:
        print('Not')

str = input()
ispalindrome(str)