# Strings are formed with single or double quotations 
my_string = "Hello, how are you today?"

my_string_2 = 'Hello, how are you today?'

# Sometimes you will want a quote mark inside the stering
# you can do something called escaping the character with a 
# backslash \
test_string = "This is Paul's car."
test_string_2 = 'This is Paul\'s car.'

# broken_string = "This doesn't work'

# Methods add features to object to do cool things with them
letter_counts = my_string.count("h")

print(letter_counts)

search_term = "a"
print(my_string.count(search_term))