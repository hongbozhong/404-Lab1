import requests
res = requests.get("http://google.com/", allow_redirects=True)
print(res.text)