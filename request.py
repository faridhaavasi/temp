import requests
import json
def get_price_bitcoin():
    page=requests.get("https://api.coinstats.app/public/v1/coins/bitcoin?currency=USD")
    json_object_string=page.json()
    #print(json_object_string)
    price=str(json_object_string['coin']['price'])
    #print(price)
    return price

print(get_price_bitcoin())

API_KEY="736E5A58587758746D4D5042553961754B7A587571592F6936617A4E37644A7346566A49465965427A49733D"
url="https://api.kavenegar.com/v1/{%s}/sms/send.json"%API_KEY
peyload={
    "receptor":"***********",
    "message":get_price_bitcoin(),
}
page=requests.post(url,json=peyload)
print(page.ok)
print(page)
