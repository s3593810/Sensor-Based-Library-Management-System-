# import MySQLdb
# from sampleinsert import SamInsert
# from add_event import Add_event
# from QRCodeScanner import QRCodeReader
# from speechRecognition import SpeechRecognition
import datetime
from datetime import datetime

event = "Add_event()"
getDetails = "SamInsert()"

class MasterDrive:
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


    search()
        Gives user search options to search a book by different criteria.

    BorrowBook()
        Handles the functionality of borrowing books 
        from the existing books list table.
    
    ReturnBook()
        Handles the functionality of a book being returned.
    
    SearchID()
        Adds search functionality by book id.
    
    SearchTitle()
        Adds search functionality for book by books title.
    
    SearchAuthor()
        Adds search functionality for books by authors name.
    
    SearchDate()
        Adds search functionality for users by particular date. 

    SearchbyQRCode()
        Adds functionality so that user can scan qr code to search or return a book.

    """
    HOST = "35.201.25.216"
    USER = "root"
    PASSWORD = ""
    DATABASE = "LMS"
    qrCode="QRCodeReader()"
    speechRecognition="SpeechRecognition()"

    def __init__(self, connection = None):
        if(connection == None):
            connection = """MySQLdb.connect(MasterDrive.HOST, MasterDrive.USER,
                MasterDrive.PASSWORD, MasterDrive.DATABASE)"""
        self.connection = connection

    

    
    def searchOptions(self,value):
        if value=="1":

            print("1.Search using keyboard")
            print("2.Search using QR code")
            print("3.Search by speech recognition")
            selection = input("Select an option: ")
            if(selection == "1"):
                return input("Enter the search key :")
            elif(selection == "2"):
                return self.qrCode.readCode() 
            elif(selection == "3"):
                return self.speechRecognition.getKeyToSearch()
        else:
            print("1.Search using keyboard")
            print("2.Search by speech recognition")
            selection = input("Select an option: ")
            if(selection == "1"):
                return input("Enter the search key :")
            elif(selection == "2"):
                return self.speechRecognition.getKeyToSearch()

    def insertUser(self, user):
        if self.isExist(user["username"])==False:
            with self.connection.cursor() as cursor:
                cursor.execute("insert into LmsUser (UserName, FirstName,LastName) values (%s,%s,%s)", (user["username"],user["firstname"],user["lastname"],))
            self.connection.commit()   

    def isExist(self, username):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT count(UserName) FROM LmsUser WHERE UserName=%s", (username,))
            result = cursor.fetchone()[0]
            if result > 0:
                return True
        return False        

    def BorrowBook(self):
        print("--------------Borrow Book---------------")
        bookid = input("Enter the Book ID ")
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT count(bookid) FROM Book WHERE BookID=%s", (bookid,))
            value = cursor.fetchone()
            
            if(value[0] == 1):
                cursor.execute("SELECT Status FROM BookBorrowed WHERE BookID=%s", (bookid,))
                
                value = cursor.fetchone()
                print(value)
                if(value == None or value[0] == "returned"):
                    userid = 1 # have to change
                    now = datetime.now()
                    date = now.strftime('%Y-%m-%d %H:%M:%S')
                    with self.connection.cursor() as cursor:
                        cursor.execute("insert into BookBorrowed (LmsUserID,BookID,Status,BorrowedDate,ReturnedDate) values (%s,%s,%s,%s,%s)", (userid,bookid,"borrowed",date,None))
                        name = getDetails.getPerson(userid)
                        book = getDetails.getBook(bookid)
                        cursor.execute("""UPDATE BookBorrowed SET Status = %s , ReturnedDate = %s WHERE BookID= %s """,("borrowed", date, bookid))
                        event.insert(name,bookid, "borrowed", date, book, userid)
                    self.connection.commit()
                    print("Book has been Borrowed ! ")
                elif(value[0] == "borrowed"):
                    print("Sorry Book has been already taken ! ")
    
    def ReturnBook(self):
        print("--------------Return Book---------------")
        bookid = input("Enter the Book ID ")
        borroweddate = input("Enter the Borrowed Date in YY - MM - DD = ")
        with self.connection.cursor() as cursor:

            cursor.execute("SELECT count(bookid) FROM Book WHERE BookID=%s", (bookid))
            value = cursor.fetchone()

            if(value[0] == 1):
                cursor.execute("SELECT Status FROM BookBorrowed WHERE BookID=%s and BorrowedDate = %s", (bookid,borroweddate,))
                value = cursor.fetchone()
                if(value == None or value[0] == "returned"):
                    print("This Book is not Borrowed ! ")
                elif(value[0] == "borrowed"):
                    now = datetime.now()
                    date = now.strftime('%Y-%m-%d %H:%M:%S')
                    with self.connection.cursor() as cursor:
                        cursor.execute("""UPDATE BookBorrowed SET Status = %s , ReturnedDate = %s WHERE BookID= %s """,("returned", date, bookid))
                    self.connection.commit()
                    print("Book has been returned ! ")
        # with self.connection.cursor() as cursor:
        #     cursor.execute("select * from BookBorrowed")
        #     print( cursor.fetchall())


    def SearchID(self,bookid):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book WHERE BookID=%s", (bookid,))
            value = cursor.fetchall()
            print(value)
            for val in value:
                print("BOOK ID = "+str(val[0])+"| TITLE = "+val[1]+"| AUTHOR = "+val[2]+"| PUBLISHED_DATE = "+str(val[3]))
    
    def SearchTitle(self, book_name):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book WHERE title=%s", (book_name,))
            print("asds")
            value = cursor.fetchall()
            for val in value:
                print("BOOK ID = "+str(val[0])+"| TITLE = "+val[1]+"| AUTHOR = "+val[2]+"| PUBLISHED_DATE = "+str(val[3]))



    def SearchAuthor(self,book_title):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book WHERE Author=%s", (book_title,))
            value = cursor.fetchall()
            for val in value:
                print("BOOK ID = "+str(val[0])+"| TITLE = "+val[1]+"| AUTHOR = "+val[2]+"| PUBLISHED_DATE = "+str(val[3]))
    
    def SearchDate(self,book_date):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book WHERE PublishedDate=%s", (book_date,))
            value = cursor.fetchall()
            for val in value:
                print("BOOK ID = "+str(val[0])+"| TITLE = "+val[1]+"| AUTHOR = "+val[2]+"| PUBLISHED_DATE = "+str(val[3]))



