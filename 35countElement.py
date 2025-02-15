def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage:
numbers = [1, 2, 3, 4, 2, 5, 2, 6]
target = 2
print(f"{target} appears {count_occurrences(numbers, target)} times in the list.")