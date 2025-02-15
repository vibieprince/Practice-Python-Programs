def evenLength(sentence):
    words = sentence.split()  # Split the sentence into words
    for word in words:
        if len(word) % 2 == 0:  # Check if the word has even length
            print(word)

# Example usage:
sentence = "Thi s is a simp  le Python program"
# sentence = "This is a simple Python program"
evenLength(sentence)