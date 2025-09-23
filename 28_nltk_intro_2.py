# let's play around with the naturla laguage toolkit
import nltk

with open('analects.txt', 'r', encoding='utf8') as rf:
    text = rf.read()

text_start = text.find("*** START OF THE PROJECT GUTENBERG EBOOK")
text_end = text.find("*** END OF THE PROJECT GUTENBERG EBOOK")

text = text[text_start:text_end]

# create an empty list to stor our information
sentences_words_tokens = []

sentences = nltk.sent_tokenize(text)

# iterate through each sentence as tokenize it into words
for sentence in sentences:
    tokenized_sentences = nltk.word_tokenize(sentence)
    sentences_words_tokens.append(tokenized_sentences)

print(sentences_words_tokens[1000:1002])

# list comprehension syntax
sent_word_tokenized = [nltk.word_tokenize(sentence) for sentence in nltk.sent_tokenize(text)]

print(sent_word_tokenized[1000:1002])