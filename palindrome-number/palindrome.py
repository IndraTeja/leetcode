def isPalindrome(x):

    if x < 0:
        return False

    rev = 0
    temp = x
    while(temp > 0):

        rev = (rev * 10) + (temp % 10)
        temp = (temp//10)

    if x == rev:
        return True
    else:
        return False


if __name__ == '__main__':
    
    x = 1991

    if isPalindrome(x):
        print(str(x) + " is a palindrome number")
    else:
        print(str(x) + " is not a palindrome number")
