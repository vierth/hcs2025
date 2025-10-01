# import libraries
import re
from class_utilities import open_file

# ==經部一 《易類》==
# actually, this is better
# 卷十三 經部十三
siku_regex = r'卷[一二三四五六七八九十百]+? *?(.)部[一二三四五六七八九十百]+?'

text = open_file("siku_catalog_edited.txt")

# if i use re.split it returns a list of the things that are divide by my regular expressions
# if i want the regex that is matched to also come back, i need a capture group

results = re.split(siku_regex, text)[1:]
structured_results = []
for i, result in enumerate(results):
    if i % 2 == 0:
        siku_cat = result
        sub_cat = re.search(r'※(.+?)類', results[i+1])
        if sub_cat == None:
            continue

        #《閩小紀》•四卷
        book_titles = re.finditer(r'《(.+?)》',results[i+1])
        for book_title in book_titles:
            if book_title == None:
                continue
                
            print(siku_cat, sub_cat.group(1), book_title.group(1))
            structured_results.append("\t".join([siku_cat, sub_cat.group(1), book_title.group(1)]))

with open('demoresults.tsv','w', encoding='utf8') as rf:
    rf.write("\n".join(structured_results))