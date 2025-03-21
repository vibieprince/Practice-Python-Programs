words = input("Enter the words seaprated by spaces : ")
content = words.split()

digitwords = []
for word in content:
    if word.isdigit():
        digitwords.append(word)

print("Words composed of digit only : ",digitwords)