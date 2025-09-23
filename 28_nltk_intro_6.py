# let's play around with the naturla laguage toolkit
import nltk
from nltk.stem.snowball import SnowballStemmer
import time

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

# create a stemmer object
stemmer = SnowballStemmer("english")
lemmatizer = nltk.WordNetLemmatizer()
start = time.time()
stemmed_words = []
for word in filtered_words:
    stemmed_words.append(stemmer.stem(word))
end = time.time()
print(end-start)

start = time.time()
lemmas = []
for word in filtered_words:
    lemmas.append(lemmatizer.lemmatize(word))
end = time.time()
print(end-start)