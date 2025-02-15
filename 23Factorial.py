def factorial(n,fact=1):
    if n == 0:
        return fact
    return factorial(n-1,n*fact)

print(factorial(1)) # 120