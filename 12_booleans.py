# boolean values let us control the flow of our programs execution
# Do one thing if something is true and another if it is false
# True or False

# Boolean statemnets are logical statements that get evaluated to True or False
# We often want to test values against each other
print(5 == 5)

# we can negate things with the !
print(5 != 5)

# Less than
print(5 < 6)

# Greater than
print(5 > 6)

# Less than or equal to
print(5 <= 6)

# greater than or equal to
print(5 >= 6)

# Are two strings the same
print("a" == "b")

# You can check if two objects are the same in momorey
list_a = ["hello"]
list_b = ["hello"]

print(list_a == list_b)
print(list_a is list_b)

print("a" is "a")
list_c = list_a
print(list_c is list_a)
print(id(list_a))