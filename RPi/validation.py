import re


class Validation:
    """
    A class used to check errors and validations

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name_regex : str
        during registration it helps checking the inserted name errors.
    userName_regex : str
        during userName insertion it helps checking the validity with 
        defined charecters in the username.
    email_regex : str
        during registration process it helps taking in valid emailid.

    Methods
    -------
    passwordValidation(password)
        Checkss if the insertede password is of particular format.

    passwordMaching(password, passConformation)
        To check if the password typed first is matching with the password types in 
        the passConfirmation prompt.
    """

    name_regex = re.compile(r'^[A-Za-z]*$')
    userName_regex = re.compile(r'^[A-Za-z0-9]*$')
    email_regex = re.compile(r'[^@]+@[^@]+\.[^@]')
    def passwordValidation(self, password):
        """
        Parameters
        ----------
        password : str
            Provided or inserted password by the user.
        
        """
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
        """
        Parameters
        ----------
        password : str
            Provided or inserted password by the user.

        passConformation: str
            Provided or inserted password by the user.
        
        """
        if password == passConformation:
            return True
        return False
