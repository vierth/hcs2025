# let's play around with the naturla laguage toolkit
import nltk

with open('analects.txt', 'r', encoding='utf8') as rf:
    text = rf.read()

text_start = text.find("*** START OF THE PROJECT GUTENBERG EBOOK")
text_end = text.find("*** END OF THE PROJECT GUTENBERG EBOOK")

text = text[text_start:text_end]

# break the text into sentences
sentences = nltk.sent_tokenize(text)

# break our text into words
words = nltk.word_tokenize(text)

print(words[200:210])