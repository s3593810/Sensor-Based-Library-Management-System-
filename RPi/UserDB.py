from datetime import datetime, timedelta
from abc import ABC
import sqlite3 as lite
from pytz import timezone


class DataBase(ABC):
    """
    DataBase class is an abstract class to create the abstract behaviors which is common in different scenarios.
    ...

    Attribute
    ----------
    _localTime : 
        This attribute takes in local time of Australia in a particular format.   
    _databaseName : 
        attribute created for the UserDB class naming _databaseName as private as the databaseName should remain the same and should not be 
        allowed to change every now and then.   
   
    Methods
    -------
    createDatabase
        Abstract Method

    insert
        Abstract Method 
    
    displayDB
        Abstract Method
        
    """
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
    """
    UserDB class is a child class of abstract class DataBase class to implement the behaviors of the abstract methods in the abstract class
    also with some additiontial behaviors thrugh different added methods as checking if user exists in the database, if the password is correct, getting 
    all user information from the database. 
    ...

    Attribute
    ----------
    It does not have an attribute it only contains methods as it is ensuring the implementation of the abstract methods.  
   
    Methods
    -------
    createDatabase
        Creates a table named user_data in the database to hold user data.

    insert(username, password, firstname, lastname, email)
        Lets user insert the data in the table as username, password, firstname, lastname, email
    
    displayDB
        Lets user print out all the data in the user_data table. 
    
    isVaildUsername_Pass(username, password)
        This method checking if the user name and password is valid or not.

    get_Pass(username)
        Gets out password from the table passing username.

    getUserInformation(username)
        This method returns user information from the database table using username.
    
    isExist(username)
        This method checks on the users existance in the system based on provided username.    
    """
    def __init__(self):
        """creating the database in the local directory using Sqlite."""
        self.createDatabase()

    def createDatabase(self):
        ""
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
