# we will often be reading and writing from python

# be very careful when you are writing to file
# because if a file exists with the same name you are using
# it will get deleted if you are writing
write_file = open("new_file.txt", "w", encoding="utf8")
write_file.write("hello friend")
write_file.close()

with open('new_file.txt', 'w', encoding="utf8") as wf:
    wf.write("hello friend")