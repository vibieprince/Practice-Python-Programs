import math
def perfectSquare(n):
    sq = math.sqrt(n)
    return sq*sq == n

n = 2
if perfectSquare(n):
    print(f"{n} is a perfect square")
else:
    print(f"{n} is not a perfect square")

