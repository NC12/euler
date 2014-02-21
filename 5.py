def is_prime(i):
    """ function to determine whether an integer is a prime number or not"""
    if i == 1:
        return False
    for divisor in range (2, int(i**0.5)+1):
        if i % divisor == 0: 
            return False
    return True

factors = []
for i in range(2, 21):
    if is_prime(i):
        factors.append(i)
    else:
        for factor in factors:
            if i % factor == 0:
                i = i // factor
        if i != 1:
            factors.append(i)

total = 1
for i in factors:
    total *= i
print(total)
