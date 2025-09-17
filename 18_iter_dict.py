# Iterating through dictionaries requires a bit more planning
my_dict = {"test":"hello", "you":"random"}

# iterating through keys
for key in my_dict.keys():
    print(key, my_dict[key])

# iterate through the values
for val in my_dict.values():
    print(val)

# iterate through both at the same time
for key, val in my_dict.items():
    print(key, val)