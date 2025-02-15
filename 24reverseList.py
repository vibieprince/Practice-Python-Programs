def rprint(lst, index=None):
    if index is None:
        index = len(lst) - 1  # Start from the last index

    if index < 0:  # Base case: Stop when index is out of range
        return

    print(lst[index])  # Print current element
    rprint(lst, index - 1)  # Recursive call for the previous element

# Example usage
my_list = [1, 2, 3, 4, 5]
print("Reversed List:")
rprint(my_list)