def createFile(name, fathername):
    with open("P.txt", "w") as file:
        file.write(name + "\n")  # Adding newline after name
        file.write(fathername + "\n")  # Adding newline after fathername

    with open("P.txt", "r") as file1:
        print(file1.read())  # Using read() instead of readlines() for better output

# Example usage:
name = str(input("Enter your name: "))
fathername = str(input("Enter your father's name: "))
createFile(name, fathername)