# w are going to write a program that identifies the most common character in a string
my_paragraph = '''CHAPTER I. 1. The Master said, 'Is it not pleasant to learn with
a constant perseverance and application?
        2. 'Is it not delightful to have friends coming from distant
quarters?'
        3. 'Is he not a man of complete virtue, who feels no
discomposure though men may take no note of him?'''

# generally we need variables to store the data we are trying to extract
most_common_character = ""
most_common_character_count = 0

# go through each character and count it
for character in my_paragraph:
    if character != " ":
        character_count = my_paragraph.count(character)
        if character_count > most_common_character_count:
            most_common_character = character
            most_common_character_count = character_count

# print the results
print(f"The most frequent character is {most_common_character}, whichc occurs {most_common_character_count} times.")