def read_file(filename):
    with open(filename, "r") as file:  # Open file in read mode
        lines = file.readlines()  # Read all lines into a list
    return lines  # Return the list of lines

# Example usage:
filename = "example.txt"  # Replace with your file name
file_content = read_file(filename)

# Print stored content
print("File contents stored in a variable:")
print("".join(file_content))  # Join list into a string for display
