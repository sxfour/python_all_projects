from urllib import request

response = request.urlopen('https://mtseti.ru')

print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)

print(response.headers)

print(response.getheaders())

print(response.headers.get('Content-Type'))
print(response.getheader('Content-Type'))
