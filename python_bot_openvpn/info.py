import base64
b_1 = 'NTQ4MjkxNjMzMDpBQUV0c2RjZVRJbzl' \
      'jdWhIc0k5M0FNcU84eDBzWHpWUkVsWQ=='
b_2 = b_1.encode('ascii')
p_1 = base64.b64decode(b_2)
p_2 = p_1.decode('ascii')