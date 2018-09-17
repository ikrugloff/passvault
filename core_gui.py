#!/usr/bin python3.6
# -*- coding: utf-8 -*-
import os
import crypt_db

password_check = crypt_db.check_master_password()

if password_check is None:
    os.system('python3.6 registration_page.py')
else:
    os.system('python3.6 login_page.py')
