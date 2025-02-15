def computeAverage(numbers):
    try:
        return sum(numbers) / len(numbers)  # Compute average
    except ZeroDivisionError:  # Handles empty list (division by zero)
        return 0.0
        
list = [1,2,3,4,5,6,7,8,9,10]
print("Average of list:",computeAverage(list)) # 5.5