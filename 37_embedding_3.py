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

lemmatizer = nltk.WordNetLemmatizer()

for text in texts:
    sentences = nltk.sent_tokenize(text)

    for sent in sentences:
        words = nltk.word_tokenize(sent.lower())
        words = [lemmatizer.lemmatize(word) for word in words if word.isalnum()]
        refined_sentences.append(words)


vec_model = gensim.models.Word2Vec(sentences=refined_sentences, vector_size=100, window=5)
# vec_model.save("word2vec.model")
# vec_model = gensim.models.Word2Vec.load('word2vec.model')

words = []
vecs = []

for word in vec_model.wv.index_to_key:
    words.append(word)
    vecs.append(vec_model.wv[word])

print(len(words))

pca = PCA()

my_pca = pca.fit_transform(vecs)

df = pd.DataFrame({"words":words, "pc1": my_pca[:,0], "pc2":my_pca[:,1]})

fig = px.scatter(df, x="pc1", y="pc2", text="words")
fig.show()