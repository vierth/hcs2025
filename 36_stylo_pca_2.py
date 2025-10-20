import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import pandas as pd
import seaborn as sns
import re

import matplotlib.pyplot as plt
from hanziconv import HanziConv

import matplotlib as mpl
mpl.rcParams['pdf.fonttype'] = 42

def chunkify(text, length=10000):
    loops = len(text)//length
    chunks = []
    for i in range(loops + 1):
        chunks.append(text[i*length:(i+1)*length])
    return chunks

def clean(text):
    text = re.sub(r'[a-zA-Z]', '', text)

    text = HanziConv.toSimplified(text)

    return text

test_division = chunkify("let's divide this up into smaller parts", length=5)

print(test_division)

color_dictionary = {"luxun":"magenta", "caoxueqin":"#000000", "zhangdai":"cyan", "shinaian":"green"}


fnames = []
texts = []
titles = []
authors = []
centuries = []




for root, dirs, files in os.walk('corpus'):
    for filename in files:
        if filename[0] == ".":
            continue

        with open(os.path.join(root, filename), 'r', encoding='utf8') as rf:
            text = rf.read()

        text = clean(text)
        
        chunks = chunkify(text)

        for chunk in chunks:
            texts.append(chunk)
            fnames.append(filename[:-4])
            labels = filename[:-4].split("_")
            authors.append(labels[0])
            titles.append(labels[1])
            centuries.append(labels[2])

'''
Some useful parameters for TfidfVector
max_features = 1000
vocabulary= ['他', '她', '我']
ngram_range = (1,1)
tokenizer = custom functino to tokenize the dcoument
analyzer = "char" or "word"
'''

vectorizer = TfidfVectorizer(use_idf=False, analyzer = "char", max_features = 100)

'''
vectorizer.fit(texts)
frequencies = vectorizer.transform(texts)
'''
frequencies = vectorizer.fit_transform(texts)

vocabulary = vectorizer.get_feature_names_out()

pca = PCA(n_components=3)

my_pca = pca.fit_transform(frequencies.toarray())
loadings = pca.components_

pc_1 = my_pca[:,0]
pc_2 = my_pca[:,1]
pc_3 = my_pca[:,2]

data = {"pc1":pc_1, "pc2": pc_2, "pc3": pc_3, "author":authors, "title":titles, "century": centuries}

df = pd.DataFrame(data)

sns.scatterplot(df, x="pc1", y="pc2", z="pc3", hue="title")

for i, word in enumerate(vocabulary):
    plt.annotate(word, xy=(loadings[0, i], loadings[1,i]))

plt.plot()