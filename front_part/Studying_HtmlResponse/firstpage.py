import requests

res = requests.get("https://www.google.com/robots.txt")

# res.headers

# res.text

# payload = {"name" : "Helloworld", "age" : 26}
# requests.post("https://webhook.site/d79f7e83-05bd-4d15-9999-78928280c180",payload)


print(res.text)
print(res.status_code)
