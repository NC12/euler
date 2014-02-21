def fibonacci():
    firstterm = 1
    secterm = 2
    curr = 2
    total = 0
    while curr < 4000000:
        if curr % 2 == 0:
            total += curr
        curr = firstterm + secterm
        firstterm = secterm
        secterm = curr
    print(total)
    
fibonacci()
