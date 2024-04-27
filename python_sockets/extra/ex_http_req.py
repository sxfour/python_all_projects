import requests

response1 = requests.get('https://mtseti.ru/')
response2 = requests.put('https://mtseti.ru/')
response3 = requests.post('https://mtseti.ru/')
response4 = requests.delete('https://mtseti.ru/')

print(response1, response2, response3, response4)
