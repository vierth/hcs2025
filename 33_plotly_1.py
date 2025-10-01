# we are going to use pandas and plotly express to create a quick data viz
import pandas as pd
import plotly.express as px

from class_utilities import open_corpus

# let's load some data in
texts, file_names= open_corpus('corpus')

# let's generate a bit of metadata out of our file_names
author, title, century = [], [], []

for file_name in file_names:
    labels = file_name.split("_")
    author.append(labels[0])
    title.append(labels[1])
    century.append(labels[2][:-4])

zhi_counts, de_counts, text_lengths = [], [], []

# extract our data
for text in texts:
    zhi_counts.append(text.count("之")/len(text))
    de_counts.append(text.count("的")/len(text))
    text_lengths.append(len(text))

# put this into a spreadsheet like format with pands
data = {"author": author, "title": title, "century":century,
        "zhi": zhi_counts, "de": de_counts, "length": text_lengths}

df = pd.DataFrame(data)

fig = px.scatter(df, x="de", y="zhi", hover_data = ["author", "title", "century"], size="length", color="author")
fig.show()