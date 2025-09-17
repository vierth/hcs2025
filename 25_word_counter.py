# w are going to write a program that identifies the most common words in a string
# but this is more efficient
ignore_words = ["", "\n", ".", ",", "a"]

my_paragraph = '''CHAPTER I. 1. The Master said, 'Is it not pleasant to learn with
a constant perseverance and application?
        2. 'Is it not delightful to have friends coming from distant
quarters?'
        3. 'Is he not a maaaaan of complete virtue, who feels no
discomposure though men may take no note of him?'''
# let's make not case sensitive
my_paragraph = my_paragraph.lower()
my_words = my_paragraph.split(" ")

# we can first get all of hte unique characters using a function called a set
unique_words = set(my_words)

# generally we need variables to store the data we are trying to extract
most_common_words = []
most_common_word_count = 0

# go through each character and count it
for word in unique_words:
    if word not in ignore_words:
        word_count = my_paragraph.count(word)
        if word_count > most_common_word_count:
            most_common_words = [word]
            most_common_word_count = word_count
        elif word_count == most_common_word_count:
            # put a bandaid on the inefficiency
            if word not in most_common_words:
                most_common_words.append(word)

# print the results
print(f"The most frequent word is {most_common_words}, which occurs {most_common_word_count} times.")

print(f"this code runs in {len(unique_words)} loops, rather than {len(my_paragraph)} loops")