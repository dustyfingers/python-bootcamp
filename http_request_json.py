import requests

url = 'https://www.icanhazdadjoke.com'
res = requests.get(url, headers={"Accept": "application/json"})
# .json() takes the string response and formats it into a python dict
print(res.json())
