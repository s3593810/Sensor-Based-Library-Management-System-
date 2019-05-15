import re


class Validation:
    name_regex = re.compile(r'^[A-Za-z]*$')
    userName_regex = re.compile(r'^[A-Za-z0-9]*$')
    email_regex = re.compile(r'[^@]+@[^@]+\.[^@]')
    def passwordValidation(self, password):

        if len(password) < 6:
            print("Make sure your password is at lest 6 letters")
            return False
        elif re.search('[0-9]', password) is None:
            print("Make sure your password has a number in it")
            return False
        elif re.search('[A-Z]', password) is None:
            print("Make sure your password has a capital letter in it")
            return False
        else:
            return True

    def passwordMaching(self, password, passConformation):
        if password == passConformation:
            return True
        return False
