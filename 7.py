def is_prime(i):
    """ function to determine whether an integer is a prime number or not"""
    if i == 1:
        return False
    for divisor in range (2, int(i**0.5)+1):
        if i % divisor == 0: 
            return False
    return True

pos = 0
number = 2
while pos < 10001:
    if is_prime(number):
        pos +=1
    number +=1

print(number - 1)
    
