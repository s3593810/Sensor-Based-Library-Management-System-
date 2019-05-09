from userDB import UserDB
from user import User
import getpass
from security import Security
import re


class Receptionist:
    __name_regex = re.compile(r'^[A-Za-z]*$')
    __db = UserDB()
    __secure = Security()

    def register(self):
        __email_regex = re.compile(r'[^@]+@[^@]+\.[^@]')
        while True:
            username = input("Insert your UserName Please: ")

            if self.__db.isExist(username) is not True and self.__name_regex.match(username):
                username.lower()
                break
            print("Sorry the username is exist.")
            print("Please choose another username")
        while True:
            password = getpass.getpass("Insert your Password Please: ")
            confirmPassword = getpass.getpass("Confierm you Password : ")
            valid = self.passwordValidation(password)
            if valid is False:
                continue
            elif password == confirmPassword:
                password = self.__secure.encrypt(password, username)
                break
            print("password does not match")
        while True:
            firstname = str(input("Insert your First Name Please: "))
            lastname = str(input("Insert your Last Name Please: "))
            if self.__name_regex.match(firstname) and self.__name_regex.match(lastname):
                break
            print("You should enter only letters")
        while True:
            email = input("Insert Your Email Please: ")
            if __email_regex.match(email):
                break
            print("you should enter a vaild email")
        user = User(username, password, firstname, lastname, email)

        self.__db.createDatabase()
        self.__db.insert(username, password, firstname, lastname, email)
        self.__db.displayDB()

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

    def login(self):
        count = 0
        while True:
            self.__db = UserDB()
            while True:
                userName = input("Insert Your User Name: ")
                if self.__name_regex.match(userName):
                    break
            password = getpass.getpass("Insert Your Password: ")
            if self.__db.isExist(userName) is False:
                print(
                    "You are not registered you should register by choose 1 from the menu")
                return False
                break
            count += 1
            result = self.__db.get_Pass(userName)
            if count == 3:
                return False
                break
            else:
                if result is not None:
                    result = result[0]
                    plain_pass = self.__secure.decrypt(result, userName)

                    if bytes.decode(plain_pass) == password:
                        print("matched")
                        data = self.__db.getUserInformation(userName)
                        print(data)
                        fName, lName = data[0]
                        return userName, fName, lName
                        break
                else:
                    print("It is wrong you can try again")
