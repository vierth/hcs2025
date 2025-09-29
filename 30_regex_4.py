# let's talk about character sets
import re

# we can create character sets (multiple options for a match)
# with square brakcets
results = re.findall(r'[abc]', " This will match a or b or c")
print(results)

# one of the cool things is that character sets can match ranges
# match a to e
r'[a-e]'
# match 0 to 9
r'[0-9]' # this is the equivelant to \d
# remember that regex are case sensitive
r'[a-zA-Z]'
r'[a-zA-Z0-9]' # this the equivelant to \w


# We can also match not things
r'[^a]'

# obviously sometimes we watch to match things that are special characters
# if we want to match a literal . we use \ to escape the charcter
r'\.'
r'\+'
r'\*'
r'\['
r'\\'