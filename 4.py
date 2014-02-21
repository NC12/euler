def is_palindrome(x):
    test = str(x)
    return test == test[::-1]

def largestpalindrome():
    largestno = 999*999
    smallestno = 100*100
    for i in range(largestno, smallestno, -1):
        if is_palindrome(i):
            for j in range(100, 999):
                if i % j ==0 and len(str(i//j)) == 3:
                    return i
print(largestpalindrome())
