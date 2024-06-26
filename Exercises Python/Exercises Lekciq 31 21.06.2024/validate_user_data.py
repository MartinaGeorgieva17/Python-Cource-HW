# Task: Valid User Name: 
# 1.At least 2 latin letters  or digit, but can not start with digit


import re

def is_valid_user_name(user_name):
    valid_user_re = re.compile(r'^[a-zA-Z][a-zA-Z0]{1,}$')
    return valid_user_re.match(user_name)



if __name__ == "__main__":
    user_name = input('Enter user name:')
    if is_valid_user_name(user_name):
        print('Welcome')
    else:
        print('Invalid name')