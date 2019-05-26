import MySQLdb


class LMScreation:
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

    createLMSuserTable()
        Creates LMS User table in the cloud database.

    createbookTable()
        Creates book table in the cloud database.

    createBookborrowedTable()
        Creates books borrowed table in cloud database
        to monitor which book is borrowed by whom and when.

    """
    HOST = "35.244.105.250"
    USER = "root"
    PASSWORD = "abc123"
    DATABASE = "LMS"

    def __init__(self, connection=None):
        if(connection == None):
            connection = MySQLdb.connect(LMScreation.HOST, LMScreation.USER,
                                         LMScreation.PASSWORD, LMScreation.DATABASE)
        self.connection = connection
        with self.connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS BookBorrowed")
            cursor.execute("DROP TABLE IF EXISTS Book")
            cursor.execute("DROP TABLE IF EXISTS LmsUser")

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def createLMSuserTable(self):
        with self.connection.cursor() as cursor:

            cursor.execute("""
                create table LmsUser (LmsUserID int not null auto_increment,
                    UserName nvarchar(256) not null,FirstName text not null,LastName text not null,
                    constraint PK_LmsUser primary key (LmsUserID),
                    constraint UN_UserName unique (UserName)
                )""")
        self.connection.commit()

    def createbookTable(self):
        with self.connection.cursor() as cursor:

            cursor.execute("""
                create table Book (BookID int not null auto_increment,
                    Title text not null,
                    Author text not null,
                    PublishedDate date not null,
                    constraint PK_Book primary key (BookID)
                )""")
        self.connection.commit()

    def createBookborrowedTable(self):
        with self.connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS BookBorrowed")
            cursor.execute("""
                create table BookBorrowed (BookBorrowedID int not null auto_increment,
                    LmsUserID int not null,
                    BookID int not null,
                    Status enum ('borrowed', 'returned'),
                    BorrowedDate date not null,
                    ReturnedDate date null,
                    Borrow int not null,
                    ReturnCount int not null,
                    EventID text null,
                    constraint PK_BookBorrowed primary key (BookBorrowedID),
                    constraint FK_BookBorrowed_LmsUser foreign key (LmsUserID) references LmsUser (LmsUserID),
                    constraint FK_BookBorrowed_Book foreign key (BookID) references Book (BookID)
                )""")
        self.connection.commit()


Lms = LMScreation()

Lms.createLMSuserTable()
Lms.createbookTable()
Lms.createBookborrowedTable()
