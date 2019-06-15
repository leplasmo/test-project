import requests


# do an url request and print the return code
r = requests.get("https://www.google.com")
# testme
print(r.status_code)
