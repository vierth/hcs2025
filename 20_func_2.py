# Sometimes we want to perform some task that gives a value us a value back
def add_numbers(num_1, num_2):
    result = num_1 + num_2
    return result

def add_numbers(num_1, num_2):
    return num_1 + num_2


res = add_numbers(1, 2)

print(res)