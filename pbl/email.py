import re

def validate(email):
    if email.count('@') == 1:
        position = email.find('@')
        if position != -1:
            recepint_name = email[:position]
            checker  = re.compile(r'^[a-zA-Z0-9](?!.*[._]{2})[a-zA-Z0-9._]{1,22}[a-zA-Z0-9]$')
            if checker.match(recepint_name):
                dot = email.find('.')
                afterposition = position + 1
                domain_name = email[afterposition:dot]
                print(domain_name)
                checkerfordomain = re.compile(r'^[a-zA-Z0-9-]{3,12}$')
                if checkerfordomain.match(domain_name):
                    return True

    return False

email = input('Input a you email:')
is_valid = validate(email)
print('Is the email valid?', is_valid)