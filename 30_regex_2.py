# we are more interested in using the keywords in regex to do fuzzy matching
import re

# sometimes we might want to match all of the numbers in a string.
# the \d special character matches 0 to 9
result = re.search(r'\d', 'It is the year 2025')
print(result)

# often we can match the opposite of a special character using a capital letter
# \D matches NOT 0 to 9
result =re.search(r'\D', 'It is the year 2025')
print(result)

# sometimes we want to match whitespace
# \s matches any whitespace character, including  new lines and tabs
result =re.search(r'\s', 'It is the year 2025')
print(result)

# \S matches NOT a whitespace
result =re.search(r'\S', 'It is the year 2025')
print(result)

# Other whitespace characters that you can search for include
# \n is a newline character
# \t is a tab charachter

# a few other useful special character
# \w will match letters or numbers
result =re.search(r'\w', 'It is the year 2025')
print(result)

# \W will match not letters or numbers
result =re.search(r'\W', 'It is the year 2025')
print(result)

# if you want to match everything, you can use the .
# this matches anything except a newline (and you can set a flag to get it to match
# new lines if you want)
result =re.search(r'.', 'It is the year 2025')
print(result)

# we can also match word boundaries with \b
result = re.search(r'\bship', "My spaceship is a ship.")
print(result)

# sometimes we want to make sure a character is optional
# we do this with a ?
result = re.search('humou?r',"This will match both humor and humour!")
print(result)

# + used in conjunction with a special character will match it one or more times
result = re.search(r'\d+', "It is the year 2025")
print(result)

# * used in conjunction wiith a special charact matches zero or more times
result = re.search(r'<p.*>', "There is some html here <p class='hello'>")
print(result)

# by default + and * are what is known as greedy
# they match the longest possible thing they can match. 
# if i want it to match the shortest possible thing I need to add a ?
result = re.search(r'<p.*?>', "There is some html here <p class='hello'> and I really like <p> elements <a> is cool too.")
print(result)