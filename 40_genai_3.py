import ollama as ol
import os
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA


ignore_files = [".DS_Store"]
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

paragraphs = []
for title, text in zip(titles, texts):
    local_paragraphs = text.split("\n\n")
    paragraphs.extend(local_paragraphs)



embeddings = ol.embed(
    model='qwen3-embedding',
    input=paragraphs[:100]
)

print(len(embeddings['embeddings'][0]))

pca = PCA(n_components=2)

my_pca = pca.fit_transform(embeddings['embeddings'])

data = {"pc1":my_pca[:,0], "pc2":my_pca[:,1], "authors":authors, "titles":titles}
df = pd.DataFrame(data)

fig = px.scatter(df, x="pc1", y="pc2", color="authors")
fig.show()