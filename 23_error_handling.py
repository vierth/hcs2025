my_dict = {"run":15, "walk":30}

try:
    my_dict['amble']
    # my_list =[1, 2, 3,4, 5]
    # print(my_list[25])
except KeyError:
    print("key does not exist")