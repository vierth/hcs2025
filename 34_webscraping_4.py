# let's use the request api to make a call to an api
import requests, time

api_url = "https://en.wikipedia.org/w/api.php"

# these days you need a user agent specificed because of ai companies scraping
headers  = {"Content-Type": "application/json", "User-Agent":"Paul Vierthaler class demo"}

# set up a call to the api
search = {
    "action":"opensearch",
    "format":"json",
    "search":"pandas"
}

search_2 = {
        "action":"query",
        "format": "json",
        "titles":"China",
        "prop":"linkshere"}
response = requests.get(api_url, params=search_2, headers=headers)
data = response.json()

with open('res.txt', 'w',encoding='utf8') as wf:
    wf.write(str(data))

while "continue" in data:
    search_2.update(data["continue"])
    # call the api
    response = requests.get(api_url, params=search_2, headers=headers)

    # get the data
    data = response.json()
    
    with open('res.txt', 'a', encoding='utf8') as af:
        af.write("\n")
        af.write(str(data))

    next_continue = data["continue"]["continue"]
    # print(data)
    time.sleep(1)