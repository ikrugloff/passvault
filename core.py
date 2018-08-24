import sys
import vault


print('<--Greetings you!-->')
print()

USERNAME = 'Gimli'
PASSWORD = 'ring'

usernameGuess = input('What is your name stranger? > ')
if usernameGuess == 'q' or usernameGuess == 'Q':
    sys.exit()

passwordGuess = input('I need a key to save your secrets... > ')
if passwordGuess == 'q' or usernameGuess == 'Q':
    sys.exit()

while True:

    if USERNAME == usernameGuess and PASSWORD == passwordGuess:
        print(f'\n<--Welcome back master {usernameGuess}!-->\n')
        for key, value in vault.mySecrets.items():
            print('*' * 22)
            print(key, ' - ', value)
            print('*' * 22)
    else:
        print('\nYou are not prepared!!!\n')

    usernameGuess = input('What is your name stranger? > ')
    if usernameGuess == 'q' or usernameGuess == 'Q':
        break
    passwordGuess = input('I need a key to save your secrets... > ')
    if passwordGuess == 'q' or usernameGuess == 'Q':
        break