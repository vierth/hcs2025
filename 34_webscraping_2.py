# let's use the request api to make a call to an api
import requests

api_url = "https://en.wikipedia.org/w/api.php"

# these days you need a user agent specificed because of ai companies scraping
headers  = {"Content-Type": "application/json", "User-Agent":"Paul Vierthaler class demo"}

# set up a call to the api
search = {
    "action":"opensearch",
    "format":"json",
    "search":"pandas"
}

# let's get all of the links leading into the Pandas software package page
search_2 = {
    "action":"query",
    "format": "json",
    "titles":"China",
    "prop":"linkshere"
}

# call the api
response = requests.post(api_url, params=search_2, headers=headers)

# get the data
data = response.json()
print(data)