def makeCapital():
    lines = []
    print("Enter text (press enter on a blank line to finish):")
    while(True):
        line = input()
        if line == "":
            break
        lines.append(line.upper())
    
    for line in lines:
        print(line)
    
makeCapital()