# if statements are useful when you want to execute code only 
# if something is true, otherwise you can skip it.

# this uses something called a code
# in python code blocks start with a colon
# and are continued with indendtation

# indentend code following an if statement only exectutes if the statemtn
# is true
# only execute if 10 is less than 20
if 10 < 20:
    print("exactly")

if 10 > 20:
    print("this code will never execute")

# This will alwayas run because it is not inside a codeblock
print("Here we are!")

if 30 < 20:
    print("This is strange, 30 isn't less than 20!")
else:
    print("Yeah, of course 30 is less than 20")

# you can also add multiple condition with elif

if 10 > 10:
    a = '10 is larger than ten'
elif 10 == 10:
    a = '10 is equal to ten'
elif 10 < 10:
    a = "10 is less than ten"
else:
    a = "something else"

print(a)

my_num = 10

if my_num > 1:
    res = "a is closest to 1"
elif my_num > 5:
    res = "a is closest to 5"
elif my_num > 8:
    res = "a is closest to 8"

print(my_num, res)