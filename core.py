import sys
import crypt_db


def main():
    password_check = crypt_db.check_master_password()

    while password_check is None:
            new_master_password = str(input('My lord, create a new master password please! >'))
            new_master_password = crypt_db.encrypt(new_master_password).decode('utf-8')
            crypt_db.create_master_password(new_master_password)
            password_check = crypt_db.check_master_password()

    print('<--Greetings you!-->')
    # print()

    USERNAME = crypt_db.get_master_login()
    PASSWORD = crypt_db.get_master_pass()

    usernameGuess = input('What is your name stranger? > ')
    if usernameGuess == 'q' or usernameGuess == 'Q':
        sys.exit()

    passwordGuess = input('I need a key to save your secrets... > ')
    if passwordGuess == 'q' or passwordGuess == 'Q':
        sys.exit()

    while True:

        if USERNAME == usernameGuess and PASSWORD == passwordGuess:
            print(f'\n<--Welcome back master {usernameGuess}!-->\n')
            crypt_db.output()
            break
        else:
            print('\nYou are not prepared!!!')

        print('\n<--Greetings you!-->')
        usernameGuess = input('What is your name stranger? > ')
        if usernameGuess == 'q' or usernameGuess == 'Q':
            break
        passwordGuess = input('I need a key to save your secrets... > ')
        if passwordGuess == 'q' or passwordGuess == 'Q':
            break

if __name__ == '__main__':
    main()
