import re
# sometimes we want to match something a specific number of times
# in this case we use curly brackets
# {3} matches something exactly three times
result = re.search(r'a{3}', 'Will we match a or aaaaaaa')
print(result)

# to match something zero to 3 times we can do this
# {0,3} or alteratively {,3}
# matching it 3 or more times
# {3,}
# we can also set exact ranges
# {3, 7} matches 3 to 7 times