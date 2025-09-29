# sometimes we would like to find everything
import re

my_string = "this string 2025 has many numbers like 18, 52, 5000, and 9000."

# findall finds all the matches and returns a list of strings
results = re.findall(r'\d+', my_string)
print(results)

# if we want match objects instead we needto use finditer
results = re.finditer(r'\d+', my_string)
for result in results:
    print(result)
print('hello, hello')
for result in results:
    print(result)