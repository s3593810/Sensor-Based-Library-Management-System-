from UserDB import UserDB
from user import User
import getpass
from security import Security
import re
from validation import Validation


class Receptionist:
    """
    Receptionist class used to represent an reception py functionality of user registration and login.

    ...

    Objects
    ----------
    __db : 
        Object created for UserDB class naming __db as protected object.   
    __secure : 
        Object created for the Security class naming __secure as protected object.   
    __valid :
        Object  created for the validation class naming __valid as protected object.   

    Methods
    -------
    register
        Lets a new user to register an account with valid user name, password, Proper name, email.

    login
        Lets the existing user login to the system using valid user id and password. 


    """
    __db = UserDB()
    __secure = Security()
    __valid = Validation()

    def register(self):
        """
        This method takes in user information as username, password and asks to user to confirm the password
        if the user name exists already in the system it asks to choose another username.
        Then the password gets checked if its a valid one or not as well as the inserted password matching the 
        confirmation password. If the password does not match the confirmation password it shows messege as password does not match.
        Further it prompts the user for first name, last name, email id and then user object gets created using User method of the UserDB class
        and get those all user inserted data as parameters.

        Using the methods of the UserDB class the database gets created, the overall data gets inserted as well in this method. 

        """
        while True:
            username = input("Insert your UserName Please: ")

            if self.__db.isExist(username) is not True and self.__valid.userName_regex.match(username):
                username.lower()
                break
            print("Sorry the username is exist.")
            print("Please choose another username")
        while True:
            password = getpass.getpass("Insert your Password Please: ")
            confirmPassword = getpass.getpass("Confirm your Password : ")
            if self.__valid.passwordValidation(password) is False:
                continue
            elif self.__valid.passwordMaching(password, confirmPassword):
                password = self.__secure.encrypt(password, username)
                break
            print("password does not match")
        while True:
            firstname = str(input("Insert your First Name Please: "))
            lastname = str(input("Insert your Last Name Please: "))
            if self.__valid.name_regex.match(firstname) and self.__valid.name_regex.match(lastname):
                break
            print("You should enter letters only")
        while True:
            email = input("Insert Your Email Please: ")
            if self.__valid.email_regex.match(email):
                break
            print("you should enter a vaild email address")
        user = User(username, password, firstname, lastname, email)
        self.__db.insert(username, password, firstname, lastname, email)
        self.__db.displayDB()

    def login(self):
        """
        This method asks user for user name and password and checks if the user name and password exists in the database
        if it finds the existing match it lets the user login the system.
        """
        count = 0
        while True:
            self.__db = UserDB()
            while True:
                userName = input("Insert Your UserName: ")
                if self.__valid.userName_regex.match(userName):
                    break
            password = getpass.getpass("Insert Your Password: ")
            if self.__db.isExist(userName) is False:
                print(
                    "You are not registered you should register by choose 1 from the menu")
                return False
                break
            count += 1
            result = self.__db.get_Pass(userName)
            if count == 4:
                return False
                break
            else:
                if result is not None:
                    result = result[0]
                    plain_pass = self.__secure.decrypt(result, userName)

                    if bytes.decode(plain_pass) == password:
                        data = self.__db.getUserInformation(userName)
                        return data
                        break
                    else:
                        print("Username or password is wrong")
                else:
                    print("It is wrong you can try again")
