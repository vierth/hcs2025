# all these are are ways of flexibly searching for patterns within texts.
# in order to use a regular expression in python we use
# the re library
import re

# we have a string that we want to search inside of
my_string= "Hello, how are you?"

# we can write regular expressions just like normal searches
result = re.search('are', my_string)
print(result)
print(result.group())
print(result.start())
print(result.end())
print(result.span())