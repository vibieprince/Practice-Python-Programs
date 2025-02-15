def makePairs(list1, list2):
    result = []
    for i in range(len(list1)):  # Assuming both lists have the same length
        result.append((list1[i], list2[i]))
    return result

# Example usage:
print(makePairs([1, 3, 5, 7], [2, 4, 6, 8]))  # Output: [(1, 2), (3, 4), (5, 6), (7, 8)]
print(makePairs([], []))  # Output: []