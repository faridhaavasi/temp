import requests

url='https://www.digikala.com/09901958794/orders/?activeTab=sent'

r=requests.get(url)
print(r.status_code)
