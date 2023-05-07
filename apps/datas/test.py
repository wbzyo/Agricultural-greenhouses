import requests
import time
import random
print(time.strftime('%Y-%m-%d %H'))
print(random.randint(1,10))
exit()
url='http://t.weather.itboy.net/api/weather/city/101100408'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}
r=requests.get(url,headers=headers)
air=r.json()
print(air)
print(air.get('time'))
print(air.get('cityInfo').get('parent'))
print(air.get('cityInfo').get('city'))
print(air.get('data')['shidu'])
print(air.get('data')['wendu'])