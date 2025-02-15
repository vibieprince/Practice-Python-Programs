def writeEvenOdd():
    with open("Input.txt", "r") as file:
        data = file.read()  # Read entire content

    numbers = data.split()  # Split by spaces to get individual numbers

    with open("EVEN.TXT", "w") as file1, open("ODD.TXT", "w") as file2:
        for num in numbers:
            if num.isdigit():  # Ensure it's a valid number
                if int(num) % 2 == 0:
                    file1.write(num + "\n")  # Write even number to EVEN.TXT
                else:
                    file2.write(num + "\n")  # Write odd number to ODD.TXT

writeEvenOdd()