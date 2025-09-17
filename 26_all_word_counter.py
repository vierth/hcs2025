# let's write a function that calculates the frequency of all words (techically count)
ignore_words = [""]

# let's load in the text itself
with open('analects.txt','r',encoding='utf8')as rf:
    text = rf.read()

# let's do some quick cleaning
text = text.lower()
text = text.replace(",", " ").replace(".", " ").replace("\n", " ")

words = text.split(' ')
unique_words = set(words)

print(len(unique_words)/len(words))

# create a dictionary to contain counts
word_counts = {}

for word in unique_words:
    if word not in ignore_words:
        word_counts[word] = words.count(word)


# let's sort these frequencies
sorted_words = sorted(word_counts, key=word_counts.get, reverse=True)

print(sorted_words)

for word in sorted_words[:10]:
    print(word, word_counts[word])
