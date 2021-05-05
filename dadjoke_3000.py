import requests

search_term = input("What do you want to search for?")

url = 'https://www.icanhazdadjoke.com/search'
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": search_term}
).json()
print(res['results'])
