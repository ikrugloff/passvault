# from core import *
import database
import sqlite3
import os, random, string
import sys
import msvcrt

conn = sqlite3.connect('vault.db')
cursor = conn.cursor()
cursor.execute("select login from master")
result = cursor.fetchall()
USERNAME = database.select_mlogin()
PASSWORD = database.select_mpassword()
# print(result)


def generation_password():     # Генерируем пароль
    length = 10
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))
    password = ''.join(random.choice(chars) for i in range(length))
    return password

while True:
    if USERNAME is null:
        generation_password()
        print(f'Для пользователя Gimli сгенерирован пароль {password}')
        print('Запомните данный пароль! Пароль восстановлению не подлежит!')

    if USERNAME is not null:
        if USERNAME == 'Gimli' and PASSWORD == 'ring':
            print(f'\n<--Welcome back master {usernameGuess}!-->\n')
            database.select_t_pass()
        else:
            print('\nYou are not prepared!!!\n')

        usernameGuess = input('\nWhat is your name stranger? > ')
        if usernameGuess == 'q' or usernameGuess == 'Q':
            break
        passwordGuess = input('I need a key to save your secrets... > ')
        if passwordGuess == 'q' or usernameGuess == 'Q':
            break











    # # Прерывание цикла, если пользователь нажал клавишу Enter, чтобы выйти
    # if msvcrt.kbhit():              # Нажата ли клавиша?
    #     key = ord(msvcrt.getch())   # Какая клавиша нажата?
    #     if key == 13:               # если Enter:
    #         break







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
