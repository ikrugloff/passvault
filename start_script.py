import os
import crypt_db

password_check = crypt_db.check_master_password()


def run():
    if password_check is None:
        os.system('python registration_page.py')
    else:
        os.system('python login_page.py')


if __name__ == '__main__':
    run()

