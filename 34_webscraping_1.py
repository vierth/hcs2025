# let's talk about how to connect to the internet with python
# there are a bunch of libraries that can do this
# i'm going to intorduce a copule of them
import requests

url = "https://en.wikipedia.org/wiki/China"
headers = {'User-Agent': 'Paul Vierthaler class demo'}


# make a request to grab a url
request = requests.get(url, headers=headers)

with open('china.html','w', encoding='utf8') as wf:
    wf.write(str(request.content))

# request.close()

# #print the contents
# print(contents)