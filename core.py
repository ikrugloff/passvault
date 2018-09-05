import sys
import database


print('<--Greetings you!-->')
print()

USERNAME = database.select_mlogin()
PASSWORD = database.select_mpassword()

usernameGuess = input('What is your name stranger? > ')
if usernameGuess == 'q' or usernameGuess == 'Q':
    sys.exit()

passwordGuess = input('I need a key to save your secrets... > ')
if passwordGuess == 'q' or usernameGuess == 'Q':
    sys.exit()

while True:

    if USERNAME == usernameGuess and PASSWORD == passwordGuess:
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