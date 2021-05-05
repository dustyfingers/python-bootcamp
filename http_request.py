import requests

url = 'https://www.facebook.com'
res = requests.get(url)
print(
    f"your request to {url} came back with a status code of {res.status_code}")
