from modules import aes

msg = input('Введите данные для шифрования (eng): ')
pwd = input('Задайте пароль: ')
cipher_text = aes.AESCipher(pwd).encrypt(msg)
print('Ciphertext:', cipher_text)
clear_text = aes.AESCipher(pwd).decrypt(cipher_text)
print('Cleartext:', clear_text)
