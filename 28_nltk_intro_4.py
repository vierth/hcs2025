# let's play around with the naturla laguage toolkit
import nltk
import matplotlib.pyplot as plt

with open('analects.txt', 'r', encoding='utf8') as rf:
    text = rf.read()

text_start = text.find("*** START OF THE PROJECT GUTENBERG EBOOK")
text_end = text.find("*** END OF THE PROJECT GUTENBERG EBOOK")

text = text[text_start:text_end]

# words in document
words = nltk.word_tokenize(text)

nltk_text = nltk.Text(words)

# find words that appear in similar contexts
# the bigger our corpus is the more meaningful 
# nltk_text.similar("humanity")

nltk_text.dispersion_plot(["is", "said", "benevolent", "humanity"])
# plt.show()

frequencies = nltk.FreqDist(nltk_text)

print(frequencies["and"])
print(frequencies.most_common(1))
print(frequencies.hapaxes())
print(nltk_text.collocations())