import requests
url='https://api.kavenegar.com/v1/0/utils/getdate.json'
r=requests.get(url)
print(r.ok)
print(r.status_code)