# for loops tend to be safer

# range is an interator
for i in range(10):
    print(i)

for i in range(2, 10):
    print(i)

for i in range(0,100,3):
    print(i)

for i in range(0,100):
    print(i)
    i += 1000
    print(i)

my_list = ["hi", "How", "are", "you"]
for item_for_fun in my_list:
    print(item_for_fun)

my_string = "Hi how are you"
for item in my_string:
    print(item)

new_list = ["a", "b", "c", "d"]

for letter in new_list:
    if letter == "c":
        print('i found the letter c')