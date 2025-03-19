import math

def isPerfectSquare(n):
    square = int(math.sqrt(n))
    return square*square == n

def isFibonacci(n):
    if n<0:
        return False
    return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)

num = int(input("Enter a number : "))
if isFibonacci(num):
    print(num,"is a fibonacci number")
else:
    print(num,"is not a fibonacci number")