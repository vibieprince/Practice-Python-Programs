def countSquares(N):
    count = 0
    num = 1
    while(num*num <= N):
        count += 1
        num += 1
    return count

# Example usage:
print(countSquares(1))   # Output: 1  (Perfect squares: [1])
print(countSquares(5))   # Output: 2  (Perfect squares: [1, 4])
print(countSquares(55))  # Output: 7  (Perfect squares: [1, 4, 9, 16, 25, 36, 49])