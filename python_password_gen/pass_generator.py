import secrets
import string
any_keys = string.digits + string.punctuation + string.ascii_letters
num = int(input('Set amount pass: '))
len = int(input('Set length pass: '))
token = secrets.token_bytes(24)
for n in range(num):
    key = ''
    for i in range(len):
        key += secrets.choice(any_keys)
    print('Passwords:', key)
print('Token: ', token)


