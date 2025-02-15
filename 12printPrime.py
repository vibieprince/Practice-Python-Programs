def printPrime(n):
    for i in range(n):
        if i < 2:
            continue
        for j in range(2,int(i**0.5+1)):
            if i % j == 0:
                break
        else:
            print(i)
        
printPrime(10) # 2 3 5 7