import MySQLdb
from datetime import datetime
import time

class SamInsert:
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

