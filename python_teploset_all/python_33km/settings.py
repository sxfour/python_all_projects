import base64

key = ["dGVzdA==", ]

key_bytes = key[0].encode("ascii")
key_ = base64.b64decode(key_bytes)
decrypted = key_.decode("ascii")
