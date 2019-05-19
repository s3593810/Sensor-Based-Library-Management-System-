import MySQLdb

class LMScreation:
    HOST = "35.189.19.149"
    USER = "root"
    PASSWORD = "Sami9305"
    DATABASE = "lms"

    def __init__(self, connection = None):
        if(connection == None):
            connection = MySQLdb.connect(LMScreation.HOST, LMScreation.USER,
                LMScreation.PASSWORD, LMScreation.DATABASE)
        self.connection = connection
        with self.connection.cursor() as cursor:
            print ("shak")
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
                    UserName nvarchar(256) not null,Name text not null,
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
                    constraint PK_BookBorrowed primary key (BookBorrowedID),
                    constraint FK_BookBorrowed_LmsUser foreign key (LmsUserID) references LmsUser (LmsUserID),
                    constraint FK_BookBorrowed_Book foreign key (BookID) references Book (BookID)
                )""")
        self.connection.commit()

Lms = LMScreation()
print("1")
Lms.createLMSuserTable()
print("2")
Lms.createbookTable()
print("3")
Lms.createBookborrowedTable()
    
    


