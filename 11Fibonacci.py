def printFibo(n,a=0,b=1):
    if n == 0:
        return
    print(a)
    printFibo(n-1,b,a+b)

printFibo(10) # 0 1 1 2 3 5 8 13 21 34