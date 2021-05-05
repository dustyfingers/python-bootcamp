import requests

url = 'https://www.icanhazdadjoke.com/search'
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "apple"}
)
# .json() takes the string response and formats it into a python dict
print(res.json())
