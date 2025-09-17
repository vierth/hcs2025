# defining functions lets us write code that is reusable.
def greetings():
    print("Hello, this is a nice function!")

# functions can take data as input
def better_greeting(name):
    print(f"Hi, my name is {name}")

# you can add as many parameters as you want
def multi_in_greeting(name_1, name_2):
    print(f"Hi {name_1}, my name is {name_2}")

def flexible_greeting(name_1, name_2, greeting_type="hello"):
    if greeting_type == "hello":
        print(f"Hi {name_1}, my name is {name_2}")
    elif greeting_type == "goodbye":
        print(f"Goodbye {name_1}, {name_2} out")
    else:
        print("I don't recognize that greeting type")


greetings()
better_greeting("Paul")
multi_in_greeting("Paul", "Ying")
res = flexible_greeting("Paul", "Ying", greeting_type="goodbye")

print(res)