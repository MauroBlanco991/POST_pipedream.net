# With this program, we can send a POST to a specific URL

import requests

url = "https://enimym529p1qj.x.pipedream.net/"
myobj = {"Hello": "World"}

x = requests.post("https://enimym529p1qj.x.pipedream.net/", json = myobj)

print(x.text)
