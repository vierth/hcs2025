# dicxtionaries are a more flexible data type that associates keys with data
my_dictionary = {}
my_dictionary = dict()

# key: value
ages = {"Paul":42, "John":22, "Ying":56}
# keys must be immutable and unique
# integers can be keys, strings, tuples
# lists cannot be keys

# get information from dictionaries with square brakets
paul_age = ages["Paul"]
print(paul_age)

# insert information into dictionaryes
ages["tom"] = 142
ages["Paul"] = 17878
# print(ages["Wei"])
print(ages.get("Wei"))
print(ages.get("Ying"))

print(ages)
