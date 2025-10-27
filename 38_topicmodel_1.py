import gensim, nltk, os, re
import logging
import pandas as pd
import plotly.express as px
import jieba
import numpy as np

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def sent_tokenize(text):
    sentences = re.split(r"[。？！：]", text)
    return sentences

def word_tokenize(text, method="word"):
    if method == "word":
        return list(jieba.cut(text))
    elif method== "char":
        return list(text)
    else:
        print("Method not recognized")
        exit()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

ignore_files = ['.DS_Store']

texts = []
authors = []
titles = []

# open our corpus
for root, dirs, files in os.walk('corpus'):
    files = [f for f in files if f not in ignore_files]

    for f in files:
        with open(os.path.join(root, f),'r', encoding='utf8') as rf:
            text = rf.read()
        
        if "START" in text:
            text = text[text.find("START OF"):text.find("END OF")]

        texts.append(text)

        file_info = f[:-4].split("_")

        authors.append(file_info[1])
        titles.append(file_info[0])

refined_sentences = []


for text in texts:
    sentences = sent_tokenize(text)

    for sent in sentences:
        words = word_tokenize(sent, method="char")
        words = [word for word in words if word.isalnum()]
        if len(words) > 0:
            refined_sentences.append(words)

corpus_dictionary = gensim.corpora.Dictionary(refined_sentences)

# i dont want to include any words that appear in fewere than two documents
# i don't want to include any words that appear in too many documents
corpus_dictionary.filter_extremes(no_below=2, no_above=.9)

# prep the corpus for topic modeling in gensim
processed_corpus = [corpus_dictionary.doc2bow(text) for text in refined_sentences]

# let's do the topic modeling
lda = gensim.models.ldamodel.LdaModel(processed_corpus, num_topics=10, id2word=corpus_dictionary, iterations=500, passes=50)

topics = lda.show_topics()
for topic in topics:
    print(topic)