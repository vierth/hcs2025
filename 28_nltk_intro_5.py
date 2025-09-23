# let's play around with the naturla laguage toolkit
import nltk
import matplotlib.pyplot as plt

with open('analects.txt', 'r', encoding='utf8') as rf:
    text = rf.read()

text_start = text.find("*** START OF THE PROJECT GUTENBERG EBOOK")
text_end = text.find("*** END OF THE PROJECT GUTENBERG EBOOK")

text = text[text_start:text_end]
text = text.lower()
# words in document
words = nltk.word_tokenize(text)

# filter the words
filtered_words = []
for word in words:
    if word.isalnum():
        filtered_words.append(word)
    
print(len(words), len(filtered_words))

'''
filtered_words = [word for word in words if word.isalnum()]
'''
# let's check total number of words
length_of_analects = len(filtered_words)
total_unique_words = len(set(filtered_words))
print(f"The analects is {length_of_analects} words long, with {total_unique_words} unique_words. This leaves a lexical diversity of {round(total_unique_words/length_of_analects,5)}")