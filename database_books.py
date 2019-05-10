import MySQLdb

class DatabaseBooks:
    HOST = "35.189.19.149"
    USER = "root"
    PASSWORD = "Sami9305"
    DATABASE = "Book"

    def __init__(self, connection = None):
        if(connection == None):
            connection = MySQLdb.connect(DatabaseBooks.HOST, DatabaseBooks.USER,
                DatabaseBooks.PASSWORD, DatabaseBooks.DATABASE)
        self.connection = connection

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def createLMSUserTable(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists LMSUser (
	                LmsUserID int not null auto_increment,
                    Name text not null,
                    constraint PK_LmsUser primary key (LmsUserID)
                
                )""")
        self.connection.commit()
    
    def createBookTable(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists Book (
	                BookID int not null auto_increment,
                    Title text not null,
                    Author text not null,
                    PublishedDate date not null,
                    constraint PK_Book primary key (BookID)
                )""")
        self.connection.commit()

    def createBookBorrowed(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists BookBorrowed (
	                BookBorrowedID int not null auto_increment,
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

    

    def insertBook(self, name, author, publish):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into Book (Title, Author, PublishedDate) values (%s, %s, %s)", (name, author, publish,))
        self.connection.commit()

        return cursor.rowcount == 1

    def getBooks(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select BookID, Title, Author, PublishedDate from Book")
            return cursor.fetchall()

    def deleteBook(self, name):
        with self.connection.cursor() as cursor:
            cursor.execute("delete from Book where Title = %s", (name,))
        self.connection.commit()

    def searchByName(self, name):
         with self.connection.cursor() as cursor:
            cursor.execute("select BookID, Title, Author, PublishedDate from Book where Title = %s", (name,))
            return cursor.fetchall()
            
    def searchByAuthor(self, author):
         with self.connection.cursor() as cursor:
            cursor.execute("select BookID, Title, Author, PublishedDate from Book where Author = %s", (author,))
            return cursor.fetchall()

    def searchByPublish(self, publish):
         with self.connection.cursor() as cursor:
            cursor.execute("select BookID, Title, Author, PublishedDate from Book where PublishedDate = %s", (publish,))
            return cursor.fetchall()

            


