import MySQLdb
from sampleinsert import SamInsert
from add_event import Add_event
import datetime
from datetime import datetime

event = Add_event()
getDetails = SamInsert()

class Menu:
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

    runMenu()
        Prints out all the master py menu options 
        for user to select.

    listPeople()
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
    HOST = "35.189.19.149"
    USER = "root"
    PASSWORD = "Sami9305"
    DATABASE = "lms"

    def __init__(self, connection = None):
        if(connection == None):
            connection = MySQLdb.connect(Menu.HOST, Menu.USER,
                Menu.PASSWORD, Menu.DATABASE)
        self.connection = connection

    def runMenu(self):
        while(True):
            print()
            print("1. Search a Book")
            print("2. Borrow a Book")
            print("3. Return a Book")
            selection = input("Select an option: ")
            print()

            if(selection == "1"):
                self.listPeople()
            elif(selection == "2"):
                self.BorrowBook()
            elif(selection == "3"):
                self.ReturnBook()
            elif(selection == "4"):
                break
            else:
                print("Invalid input - please try again.")

    def listPeople(self):
        print("1.Search by ID")
        print("2.Search by Title")
        print("3.Search by Author")
        print("4.Search by PublishedDate")
        
        selection = input("Select an option: ")
        if(selection == "1"):
                self.SearchID()
        elif(selection == "2"):
                self.SearchTitle()
        elif(selection == "3"):
                self.SearchAuthor()
        elif(selection == "4"):
                self.SearchDate()
    
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

                    
                    
                




    def SearchID(self):
        book_id = input("Enter Book ID : ")
        bookid = int(book_id)
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book WHERE BookID=%s", (bookid,))
            value = cursor.fetchall()
            print(value)
            for val in value:
                print("BOOK ID = "+str(val[0])+"| TITLE = "+val[1]+"| AUTHOR = "+val[2]+"| PUBLISHED_DATE = "+str(val[3]))
    
    def SearchTitle(self):
        book_name = input("Enter title name : ")
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book WHERE title=%s", (book_name,))
            print("asds")
            value = cursor.fetchall()
            for val in value:
                print("BOOK ID = "+str(val[0])+"| TITLE = "+val[1]+"| AUTHOR = "+val[2]+"| PUBLISHED_DATE = "+str(val[3]))



    def SearchAuthor(self):
        book_title = input("Enter Author name : ")
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book WHERE Author=%s", (book_title,))
            value = cursor.fetchall()
            for val in value:
                print("BOOK ID = "+str(val[0])+"| TITLE = "+val[1]+"| AUTHOR = "+val[2]+"| PUBLISHED_DATE = "+str(val[3]))
    
    def SearchDate(self):
        book_date = input("Enter Date : ")
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book WHERE PublishedDate=%s", (book_date,))
            value = cursor.fetchall()
            for val in value:
                print("BOOK ID = "+str(val[0])+"| TITLE = "+val[1]+"| AUTHOR = "+val[2]+"| PUBLISHED_DATE = "+str(val[3]))


menu_object = Menu()
menu_object.runMenu()
