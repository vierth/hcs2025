# w are going to write a program that identifies the most common character in a string
ignore_chars = [" ", "\n", ".", ","]

my_paragraph = '''CHAPTER I. 1. The Master said, 'Is it not pleasant to learn with
a constant perseverance and application?
        2. 'Is it not delightful to have friends coming from distant
quarters?'
        3. 'Is he not a maaaaan of complete virtue, who feels no
discomposure though men may take no note of him?'''

# generally we need variables to store the data we are trying to extract
most_common_characters = []
most_common_character_count = 0

# go through each character and count it
for character in my_paragraph:
    if character not in ignore_chars:
        character_count = my_paragraph.count(character)
        if character_count > most_common_character_count:
            most_common_characters = [character]
            most_common_character_count = character_count
        elif character_count == most_common_character_count:
            most_common_characters.append(character)

# print the results
print(f"The most frequent character is {most_common_characters}, whichc occurs {most_common_character_count} times.")