# we will often be reading and writing from python

# be very careful when you are writing to file
# because if a file exists with the same name you are using
# it will get deleted if you are writing
write_file = open("new_file.txt", "w", encoding="utf8")
write_file.write("hello friend")
write_file.close()

with open('new_file.txt', 'w', encoding="utf8") as wf:
    wf.write("hello friend")

# i can open files in read mode with the 'r' flag
with open('new_file.txt','r', encoding='utf8') as rf:
    text = rf.read()

print(text)

# you can append to a file with the 'a' flag
with open('new_file_2.txt','a', encoding='utf8') as af:
    af.write("this adds information.")