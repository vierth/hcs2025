# we can add things to list with append
my_list = [1, 2, 3, 4, 5]

my_list.append(10)

print(my_list)

# remove things from lists with pop
deleted_number = my_list.pop()

print(my_list, deleted_number)

# remove things from a specific place
my_list.pop(1)
print(my_list)

# insert things at specific places
my_list.insert(1,80)
print(my_list)

# overwrite a value at an index
my_list[3] = 400
print(my_list)