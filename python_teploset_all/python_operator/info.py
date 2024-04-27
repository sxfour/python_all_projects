import base64
from config import main_lib


b_1 = main_lib[0]
b_2 = b_1.encode('ascii')
p_1 = base64.b64decode(b_2)
p_2 = p_1.decode('ascii')