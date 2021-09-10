import requests
res = requests.get("https://raw.githubusercontent.com/hongbozhong/404-Lab1/master/curl_script.py", allow_redirects=True)
open("curl_script_copy.py", "wb").write(res.content)
print(res.text)