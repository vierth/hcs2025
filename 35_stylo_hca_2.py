import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from hanziconv import HanziConv

color_dictionary = {"luxun":"magenta", "caoxueqin":"#000000", "zhangdai":"#dedede", "shinaian":"teal"}


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

        simplified = HanziConv.toSimplified(text)

        texts.append(simplified)
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



print(vectorizer.get_feature_names_out())

# calculate the text similarities
simlarities = cosine_similarity(frequencies)

# calculate the clusters
linkages = linkage(simlarities, "ward")

dendrogram(linkages, labels=authors, orientation="right", leaf_font_size=8, leaf_rotation=45)

ax = plt.gca()
labels = ax.get_ymajorticklabels()

for label in labels:
    label.set_color(color_dictionary[label.get_text()])

plt.show()
