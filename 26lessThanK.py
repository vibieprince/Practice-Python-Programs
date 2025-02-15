def lessThanK(arr,k):
    list = []
    for i in arr:
        if i<k:
            list.append(i)
    return list

# Example usage
arr = [1, -2, 0, 5, -3]
k = 0
print(lessThanK(arr,k)) # [1, 2, 3, 4]