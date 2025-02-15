# Taking input from the user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"\nBefore swapping: a = {a}, b = {b}")

# Swapping without a temporary variable
a, b = b, a  

print(f"After swapping: a = {a}, b = {b}")
