words = input("Enter words separated by commas : ")
sorted_words = sorted(word.strip() for word in words.split(','))
result = ", ".join(sorted_words)

print(result)


# input : without, hello, bag, world 
# output : bag, hello, without, world