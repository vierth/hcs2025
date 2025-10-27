import gensim, nltk, os
import logging
import pandas as pd
import plotly.express as px

from sklearn.decomposition import PCA

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

ignore_files = ['.DS_Store']

texts = []
authors = []
titles = []

# open our corpus
for root, dirs, files in os.walk('fedpapers'):
    files = [f for f in files if f not in ignore_files]

    for f in files:
        with open(os.path.join(root, f),'r', encoding='utf8') as rf:
            text = rf.read()
        
        texts.append(text)

        file_info = f[:-4].split("_")

        authors.append(file_info[1])
        titles.append(file_info[0])

refined_sentences = []

for text in texts:
    sentences = nltk.sent_tokenize(text)

    for sent in sentences:
        words = nltk.word_tokenize(sent.lower())
        print(words)
        refined_sentences.append(words)


vec_model = gensim.models.Word2Vec(sentences=refined_sentences, vector_size=100, window=5)

vec_model.save('word2vec.model')

vec_model.wv.save('word2vec.wordvectors')

print(vec_model.wv.most_similar('freedom', topn=25))