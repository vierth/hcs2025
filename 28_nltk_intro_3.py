# let's play around with the naturla laguage toolkit
import nltk

with open('analects.txt', 'r', encoding='utf8') as rf:
    text = rf.read()

text_start = text.find("*** START OF THE PROJECT GUTENBERG EBOOK")
text_end = text.find("*** END OF THE PROJECT GUTENBERG EBOOK")

text = text[text_start:text_end]

# words in document
words = nltk.word_tokenize(text)

nltk_text = nltk.Text(words)

print(nltk_text)

# create a concordance
nltk_text.concordance("said")

# specify number of results and width of context
nltk_text.concordance("said", width=79, lines=100)