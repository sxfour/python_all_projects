import secrets
import string
import time

design = '-' * 28


class PasswdGen:
    def __init__(self, amount, longer):
        self.longer = longer
        self.amount = amount
        """Formula generator"""
        self.generate_key = string.digits + string.ascii_uppercase + string.punctuation

    def build(self):
        try:
            for n in range(self.longer):
                key = ''
                for i in range(self.amount):
                    key += secrets.choice(self.generate_key)
                print('Password:', key)
        except:
            print('Error command!')


class Double:
    pass


class Triple:
    pass


class Token:
    pass


print(design + '\n  Passwords generator v0.1\n' + design)
time.sleep(1.3)
PasswdGen1 = PasswdGen(12, 10)
PasswdGen1.build()
