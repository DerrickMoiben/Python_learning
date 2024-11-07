def validate(email):
    if email.count('@') == 1:
        return True

    return False

email = input('Input a you email:')
is_valid = validate(email)
print('Is the email valud?', is_valid)