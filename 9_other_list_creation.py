# we can turn strings into lists very easily
my_string = "My name is Paul Vierthaler."

a_list = list(my_string)

print(a_list)

# we can create this list with more control with split
word_list_sortof = my_string.split(" ")
print(word_list_sortof)

# We can join lists into to strijgs with the join method
recovered_string = " ".join(word_list_sortof)
print(recovered_string)