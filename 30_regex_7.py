import re

# sometimes we want to match one thing or another
print(re.search(r'cat|dog|rat', "this will match rat and cat?"))

# we also might want to replace things
my_string = "My      name is Paul      Vierthaler."
print(my_string)
my_string = re.sub(r'\s+', " ", my_string)
print(my_string)

my_string_2 = "Oh captain, my captain, are you a general?"

added_tags = re.sub(r'(captain|general)', "<tag>\g<1></tag>", my_string_2)
print(added_tags)