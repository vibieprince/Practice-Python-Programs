def checkPrime(n):
    for i in range(2,int(n**0.5+1)):
        if(n%i==0):
            return False
    return True

print(checkPrime(9)) # True
print(checkPrime(19)) # False