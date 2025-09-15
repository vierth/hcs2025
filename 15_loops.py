# in many cases we want to run code multiple times
# While loops execute as long as the statement is true

i = 0
while i < 10:
    print(i)
    i = i + 1
    # i += 1

# we can accidentally create an infinte loop
# i = 0
# while i < 10:
#     print(i)
#     i -= 1

while True:
    # keep doing something forever until the program has a reason to quite
    exit()