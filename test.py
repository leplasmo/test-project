import requests


# do an url request and print the return code
r = requests.get("http://www.province.luxembourg.be")
# testme
print(r.status_code)
