# from core import *
# from database import *
import os, random, string




if __name__ == "__main":

    if



    else if USERNAME != usernameGuess:
    # Простой вариант генерации паролей
    length = 10
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))
    print(''.join(random.choice(chars) for i in range(length)))




"""
Альтернативный способ генерации пароля
"""
# import M2Crypto
# import string
# def random_password(length=10):
#     chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
#     password = ''
#     for i in range(length):
#         password += chars[ord(M2Crypto.m2.rand_bytes(1)) % len(chars)]
#     return password
