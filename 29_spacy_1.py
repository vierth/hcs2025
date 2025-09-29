'''
to install spacy you will neeed to run this in your terminal

pip install spacy

downloading the models themselves

python -m spacy download en_core_web_sm
python -m spacy download zh_core_web_sm
python -m spacy download zh_core_web_trf
'''

import spacy
from spacy import displacy
from class_utilities import open_file

nlp = spacy.load('en_core_web_sm')

text = open_file('analects.txt')

text = text[text.find("*** START"):text.find("*** END")]

document = nlp(text)

# for ent in document.ents:
#     print(ent.text, ent.label_)

for sentence in document.sents:
    sentence

for noun_chunk in document.noun_chunks:
    noun_chunk

for word in document:
    pass
    # print(word.text, word.pos_, word.dep_, word.lemma_)

# print(spacy.explain("advcl"))

# displacy.serve(document, style='ent', port=8080)