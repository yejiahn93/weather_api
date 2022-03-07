#Weather API
import requests
import json

info = '''
1. Los Angeles
2. New York
3. Georgia
'''
print(info)
inputVal = input('put the number:')
cityName = 'los-angeles'

if  int(inputVal) ==2:
    cityName = 'new-york'
elif int(inputVal) ==3:
    cityName = 'georgia'
else:
    cityName = 'los-angeles'


response = requests.get('http://api.weatherapi.com/v1/current.json?key=b4e8569369b14922abd185346220703&q='+ cityName +'&aqi=yes')
jsonObj = json.loads(response.text)

print(cityName, 'Temperature is',jsonObj['current']['temp_c'],'Status is',jsonObj['current']['condition']['text'])

