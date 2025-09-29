# We can extract information from regular expression matches using
# groups
import re

# groups are formed in regexes with () parantheses
some_html = "<a href='www.baidu.com'> and also <a href='google.com'>"

result = re.search(r'www\..+?\.com', some_html)
print(result)

results = re.finditer(r"<a href='.+?'>", some_html)

for result in results:
    print(result)

# i can capture JUST the url if I watnt
results = re.finditer(r"<a href='(.+?)'>", some_html)

for result in results:
    print(result.group(0), result.group(1))
