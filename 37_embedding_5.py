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
        refined_sentences.append(words)


vec_model = gensim.models.Word2Vec(sentences=refined_sentences, vector_size=100, window=5)
# vec_model.save("word2vec.model")
# vec_model = gensim.models.Word2Vec.load('word2vec.model')

vocab = []
vecs = []

for word in vec_model.wv.index_to_key:
    vocab.append(word)
    vecs.append(vec_model.wv[word])


vecs = np.array(vecs)

tsne = TSNE(n_components=2, learning_rate='auto', init='random', perplexity=3)

#if the following line of code is producing an error, it is likely because
# of a bug in the threadpoolctl library
# I fixed it by installing threadpoolctl 3.1.0
# pip install threadpoolctl==3.1.0
my_tsne = tsne.fit_transform(vecs)

df = pd.DataFrame({"words":vocab, "dim_1": my_tsne[:,0], "dim_2":my_tsne[:,1]})

fig = px.scatter(df, x="dim_1", y="dim_2", text="words")
fig.show()