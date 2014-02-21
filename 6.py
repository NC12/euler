sumofsquares = 0
squareofsum = 0
for i in range(1, 101):
    sumofsquares += i**2
    squareofsum += i
squareofsum = squareofsum**2
print(squareofsum - sumofsquares)
    
