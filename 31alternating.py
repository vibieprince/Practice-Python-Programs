def alternating(list):
    if not list:
        return True
    if list[0] % 2 == 0:
        for i in range(1,len(list)):
            if(list[i] % 2 == list[i-1] % 2):
                return False
        return True
    
# Example usage:
print(alternating([10, 9, 9, 6]))  # False
print(alternating([10, 15, 8]))    # True
print(alternating([10]))           # True
print(alternating([]))             # True