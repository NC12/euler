# function to find sum of all multiples of 3 or 5 below 1000
# initialise variable to store sum
total = 0
for i in range(1000):
    # check if number is divisible by 3 or 5
    if i % 3 == 0 or i % 5 == 0:
        # add to sum
        total += i
print(total)
        
    
