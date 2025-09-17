# w are going to write a program that identifies the most common character in a string
# but this is more efficient
ignore_chars = [" ", "\n", ".", ","]

my_paragraph = '''CHAPTER I. 1. The Master said, 'Is it not pleasant to learn with
a constant perseverance and application?
        2. 'Is it not delightful to have friends coming from distant
quarters?'
        3. 'Is he not a maaaaan of complete virtue, who feels no
discomposure though men may take no note of him?'''
# let's make not case sensitive
# my_paragraph = my_paragraph.lower()


# we can first get all of hte unique characters using a function called a set
unique_chars = set(my_paragraph)

# generally we need variables to store the data we are trying to extract
most_common_characters = []
most_common_character_count = 0

# go through each character and count it
for character in unique_chars:
    if character not in ignore_chars:
        character_count = my_paragraph.count(character)
        if character_count > most_common_character_count:
            most_common_characters = [character]
            most_common_character_count = character_count
        elif character_count == most_common_character_count:
            # put a bandaid on the inefficiency
            if character not in most_common_characters:
                most_common_characters.append(character)

# print the results
print(f"The most frequent character is {most_common_characters}, whichc occurs {most_common_character_count} times.")

print(f"this code runs in {len(unique_chars)} loops, rather than {len(my_paragraph)} loops")