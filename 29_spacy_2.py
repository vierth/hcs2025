# do some corpus level nlp on chinese docs
import spacy
import os
import class_utilities as util

# result directory
save_dir = "spacy_res"
if not os.path.isdir(save_dir):
    os.mkdir(save_dir)

# load the texts in the corpus folder into variables
texts, file_names = util.open_corpus("corpus")

# create nlp object using the transformer model for chinese
nlp = spacy.load("zh_core_web_trf")

# go through each file and analyze it
for text,f_name in zip(texts, file_names):

    # clear off gutenberg boilerplate
    text = text[text.find("*** START"):text.find("*** END")]

    # create document object with nlp object
    document = nlp(text)

    # get each word's text and its part of speech and put it into a list of strings
    # that are delimited with tab characters
    info = [f"{word.text}\t{word.pos_}" for word in document]

    # create a file path to save results
    save_path = os.path.join(save_dir, f"{f_name[:-4]}_res.txt")

    # write the results to file
    with open(save_path,'w',encoding='utf8') as wf:
        wf.write("\n".join(info))

