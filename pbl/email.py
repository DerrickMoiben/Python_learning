import re

def validate(email):
    if email.count('@') == 1:
        position = email.find('@')
        if position != -1:
            recepint_name = email[:position]
            checker  = re.compile(r'[a-zA-Z0-9](?!.*[._]){2}[a-zA_Z0-9._]{1,22}[a-zA-Z0-9]@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$')
            if checker.match(recepint_name):
                return True

    return False

email = input('Input a you email:')
is_valid = validate(email)
print('Is the email valud?', is_valid)