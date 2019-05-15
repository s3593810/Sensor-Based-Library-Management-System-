from userDB import UserDB
from user import User
import getpass
from security import Security
import re
from validation import Validation


class Receptionist:
    
    __db = UserDB()
    __secure = Security()
    __valid= Validation()

    def register(self):
        
        while True:
            username = input("Insert your UserName Please: ")

            if self.__db.isExist(username) is not True and self.__valid.userName_regex.match(username):
                username.lower()
                break
            print("Sorry the username is exist.")
            print("Please choose another username")
        while True:
            password = getpass.getpass("Insert your Password Please: ")
            confirmPassword = getpass.getpass("Confierm you Password : ")
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
            print("You should enter only letters")
        while True:
            email = input("Insert Your Email Please: ")
            if self.__valid.email_regex.match(email):
                break
            print("you should enter a vaild email")
        user = User(username, password, firstname, lastname, email)

        self.__db.createDatabase()
        self.__db.insert(username, password, firstname, lastname, email)
        self.__db.displayDB()

    def login(self):
        count = 0
        while True:
            self.__db = UserDB()
            while True:
                userName = input("Insert Your User Name: ")
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
