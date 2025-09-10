# String concatenation is when we add strings together
my_string = "Hello, friend! oooooooo"
second_string = "How are you? are oooooo"

new_string = my_string + " " + second_string

print(new_string)

# string concat works with numbers if they are strings
num_1 = "1234"
num_2 = "5678"
num_3 = num_1 + num_2
print(num_3)

# get length of string
print(len(my_string))

print(my_string[0])
print(my_string[10])
# print(my_string[400])
print(my_string[-1])
print(my_string[-2])
print(my_string[0:10])
print(my_string[8:])
print(my_string)
my_string = my_string[:10]
print(my_string)

# finding a substring is very easy, we use the find method
print(second_string.find("are"))  

# we can replace characters eaasily
second_string = second_string.replace('o', "a")
print(second_string)


my_string.isalnum()
"123.5".isdecimal()
"123".isnumeric()

print("this is all lowercase".upper())
print("this is all UPPERCASE".lower())
print("this is all UPPERCASE".capitalize())

# there are format strings in python that let us insert variables into strings

python_version = "3.11"

print(f"The version of python I am using is {python_version}")
print("The version of python I am using is " + python_version)