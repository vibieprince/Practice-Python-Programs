import re

def filterNumbers(words):
    # Removes all numbers from the list of words
    filtered_words = []
    for word in words:
        if not word.isdigit():
            filtered_words.append(word)
    return filtered_words

def filterWordsString(words):
    # Removes word that start with a vowel (a,e,i,o,u)
    filtered_words = []
    for word in words:
        if not re.match(r'^[AEIOUaeiou]',word):
            filtered_words.append(word)
    return filtered_words

def filter_nouns(words):
    # Removes specific words (Agra,Ramesh,Tomato,Patna)
    nouns = ["Agra","Ramesh","Tomato","Patna"]
    filtered_words = []
    for word in words:
        if word not in nouns:
            filtered_words.append(word)
    return filtered_words

def cleanText(text):
    # Applies all filters to the text
    words = text.split()
    words = filterNumbers(words)
    words = filter_nouns(words)

    cleaned_text = " ".join(words)
    return cleaned_text

text = "Agra is a city in India with 1234 people. Ramesh lives there. Tomato is red. 89 Patna."

print("Cleaned Text : ",cleanText(text))