import MySQLdb
from datetime import datetime
import time

class SamInsert:
    
    """
    This class shows the cloud managment and database 
    functionalities.

    
    Attributes
    ----------

    HOST
        IP address of the Host device.
    USER
        UserName for the Cloud database.
    PASSWORD
        Password for the cloud database.
    DATABASE
        Name of the database already created in cloud.
        
    Methods
    -------
    __init__(connection=None)
        Checks on the connection and selects cursor 
        cleans up the database if there is already tables exist.

    close()
        Closes the connection.
    __enter__()

    __exit__()

    insertUser(name, nick)
        Creates a user for LMS User table in the cloud database
        based on the given username and name of the user.

    insertBook(name, author, time)
        Creates a book based on provided title, author name of the 
        book and the time in book table in the cloud database.

    getPeople()
        This method helps getting the username and name of the user 
        from the LMS User table.
    
    getPerson(id)
        This method helps getting the username and name from lms user table
        based on provided users id.

    getBook(id)
        This method helps getting the book information from book table
        based on provided book id.


    """

    HOST = "35.189.19.149"
    USER = "root"
    PASSWORD = "Sami9305"
    DATABASE = "lms"

    
    def __init__(self, connection = None):
        if(connection == None):
            connection = MySQLdb.connect(SamInsert.HOST, SamInsert.USER,
                SamInsert.PASSWORD, SamInsert.DATABASE)
        self.connection = connection

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()


    def insertUser(self, name, nick):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into LmsUser (UserName,Name) values (%s,%s)", (name,nick,))
        self.connection.commit()

    def insertBook(self, name, author, time):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into Book (Title,Author,PublishedDate) values (%s,%s,%s)", (name,author,time,))
            print("testing.....")
        self.connection.commit()

    def getPeople(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select UserName, Name from LmsUser")
            return cursor.fetchall()

    def getPerson(self, id):
        with self.connection.cursor() as cursor:
            print("Testing")
            cursor.execute("select UserName, Name from LmsUser where LmsUserID = %s",(id,))
            print(cursor)
            return cursor.fetchall()
    
    def getBook(self, id):
        with self.connection.cursor() as cursor:
            cursor.execute("select * from Book where BookID=%s",(id,))
            return cursor.fetchall()

