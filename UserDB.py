from datetime import datetime, timedelta
from abc import ABC
import sqlite3 as lite
from pytz import timezone


class DataBase(ABC):
    _localTime = datetime.now(
        timezone('Australia/Sydney')).strftime("%Y-%m-%d %H:%M:%S")
    _databaseName = 'user.db'
    #   @abstractmethod

    def createDatabase(self):
        pass
#   @abstractmethod

    def insert(self):
        pass
#   @abstractmethod

    def displayDB(self):
        pass

class UserDB(DataBase):

    def createDatabase(self):
        connection = lite.connect(self._databaseName)
        with connection:
            point = connection.cursor()
            point.execute(
                "CREATE TABLE IF NOT EXISTS user_data(timestamp DATETIME, username VARCHAR(20), password VARCHAR(20), firstname VARCHAR(30), lastname VARCHAR(30), email VARCHAR(50))")

    def insert(self, username, password, firstname, lastname, email):
        connection = lite.connect(self._databaseName)
        with connection:
            connection.execute(
                "INSERT INTO user_data values((?), (?), (?), (?), (?), (?))", (self._localTime, username, password, firstname, lastname, email,))
            connection.commit()
        connection.close()

    def displayDB(self):
        connection = lite.connect(self._databaseName)
        with connection:
            point = connection.cursor()
            print("\nEntire database contents:\n")
            for row in point.execute("SELECT * FROM user_data"):
                print(row)
        connection.close()

class Receptionist:
    def register(self):
        username=input("Insert your UserName Please: ")
        password=input("Insert your Password Please: ")
        firstname=input("Insert your First Name Please: ")
        lastname=input("Insert your Last Name Please: ")
        email=input("Insert Your Email Please: ")
        db = UserDB()
        db.createDatabase()
        db.insert(username, password, firstname, lastname, email)
        db.displayDB()

re= Receptionist()
re.register()