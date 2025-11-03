import os
from transformers import AutoTokenizer, AutoModel
import numpy as np
import plotly.express as px
from sklearn.decomposition import PCA
import pandas as pd

def get_word_positions(words):
    word_ids = [tokenizer.vocab[word] for word in words]
    word_positions = np.where(np.isin(all_word_ids, word_ids))[0]
    return word_positions

def get_context(word_id, window_size=10):
    """get tokens that occure before and after word position"""
    start_pos = max(0, word_id-window_size) # token that starts the view
    end_pos = min(word_id + window_size+1, len(all_word_ids))

    tokens = [word_lookup[word] for word in all_word_ids[start_pos:end_pos]]
    return "".join(tokens)

terms_to_search = ["云", "曰", "說", "道"]

# much of this is adapted from this notebook:
# https://colab.research.google.com/drive/1r_eoi8CMea_a3YjWC1M4EmTqKMGVMbzQ

tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-chinese")
model = AutoModel.from_pretrained("google-bert/bert-base-chinese")

ignore_files =['.DS_Store']

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

paragraphs = paragraphs[:500]

# keep track of word ids on a per document bassi
doc_word_ids = []
doc_word_vectors = []

# Ignore bert specific tokens
start_of_words = 1
end_of_words = -1

for i, doc in enumerate(paragraphs):
    print(i)
    # tokenize the text to feed into the model
    inputs = tokenizer(doc, return_tensors='pt', truncation=True, padding=True, max_length=512)

    # this is functionally identical to me doing this:
    # model(input_ids=inputs['input_ids'], 'token_type_ids=inputs['token_type_ids'], 'attention_mask'=inputs['attention_mask'])
    outputs = model(**inputs)

    doc_word_ids.append(inputs.input_ids[0].numpy()[start_of_words:end_of_words])
    doc_word_vectors.append(outputs.last_hidden_state[0, start_of_words:end_of_words,:].detach().cpu().numpy())
    # print(doc[:20], inputs)

all_word_ids = np.concatenate(doc_word_ids)
all_word_vectors = np.concatenate(doc_word_vectors, axis=0)

word_lookup = np.empty(tokenizer.vocab_size, dtype="O")
for word, index in tokenizer.vocab.items():
    word_lookup[index] = word

contexts = []
vectors = []
used_words = []

word_positions = get_word_positions(terms_to_search)

for position in word_positions:
    contexts.append(get_context(position))
    vectors.append(all_word_vectors[position])
    used_words.append(word_lookup[all_word_ids[position]])

pca = PCA(n_components=2)
pca.fit(np.array(vectors).T)

df = pd.DataFrame({"pc1":pca.components_[0,:], "pc2":pca.components_[1,:], "context":contexts, "word":used_words})

fig = px.scatter(df, x="pc1", y="pc2", color="word", hover_data=["word", "context"])
fig.show()