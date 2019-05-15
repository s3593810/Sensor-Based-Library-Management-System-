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
    def __init__(self):
        self.createDatabase()

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

    def isVaildUsername_Pass(self, username, password):
        connection = lite.connect(self._databaseName)
        with connection:
            point = connection.cursor()
            point.execute(
                "SELECT count(*) from user_data where username=(?) and password=(?)", (username, password))
            result = point.fetchone()[0]
            if result > 0:
                return True
        connection.close()
        return False

    def get_Pass(self, username):
        connection = lite.connect(self._databaseName)
        with connection:
            point = connection.cursor()
            point.execute(
                "SELECT password from user_data where username=(?)", (username,))
            
            result = point.fetchone()
        connection.close()
        return result

    def getUserInformation(self,username):
        connection = lite.connect(self._databaseName)
        with connection:
            point = connection.cursor()
            point.execute(
                "SELECT username, firstname, lastname from user_data where username=(?)", (username,))
            result = point.fetchone()
        connection.close()
        return { "username": result[0], "firstname": result[1], "lastname": result[2]  }

    def isExist(self, username):
        connection = lite.connect(self._databaseName)
        with connection:
            point = connection.cursor()
            point.execute(
                "SELECT count(*) from user_data where username=(?)", (username,))
            result = point.fetchone()[0]
            if result > 0:
                return True
        connection.close()
        return False
