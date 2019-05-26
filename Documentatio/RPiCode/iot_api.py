from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json
from flask import current_app as app

api = Blueprint("api", __name__)

db = SQLAlchemy()
ma = Marshmallow()

# Declaring the model.
class Book(db.Model):
    """
    This class loads in the data in the cloud database using api calls.

    
    Attributes
    ----------

    BookID: int 
        Collumn for Auto Generated Book Id for each time a book is added.
    Title: str
        Collumn for user (LMS Admin) inserted Book titles.
    Author: str
        Collumn for User inserted Author Name of the book.
    PublishedDate: DateTime
        DateTime collumn to monitor the dates and times when 
        book is borrowed and returned.
        
    Methods
    -------
    __init__(Title, Author, PublishedDate,BookID = None)
        This method just initializes the values for the inserted collumns. 

    
    """
    __tablename__ = "Book"
    BookID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Title = db.Column(db.Text)
    Author = db.Column(db.Text)
    PublishedDate = db.Column(db.DateTime)
    # Username = db.Column(db.String(256), unique = True)

    def __init__(self,  Title, Author, PublishedDate,BookID = None):
        self.BookID = BookID
        self.Title = Title
        self.Author = Author
        self.PublishedDate = PublishedDate

class BookSchema(ma.Schema):
    """
    This calss takes in the fields for each books using nested class named meta
    and calling the bookschema object the book information is saved. 

    """
    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, strict = True, **kwargs):
        super().__init__(strict = strict, **kwargs)
    
    class Meta:
        # Fields to expose.
        fields = ("BookID", "Title","Author","PublishedDate")

bookSchema = BookSchema()
booksSchema = BookSchema(many = True)

# Declaring the model.
class BookBorrow(db.Model):
    """
    This class setsup the modle for the borrow book api functions. 


    Attributes
    ----------

   __tablename__:  str
        Adds in the table named as BookBorrowed in the database.
    LmsUserID: str
        Collumn named LmsUserID gets created in the Bookborrowed table 
        so that each time a book is borrowed the user ID gets saved in the 
        database.
    BookID: int
        Collumn named BookID gets created in the table.
    Status: str
        Collumn named status gets created in the table
        to store information about if the book is available to 
        borrow or not.
    BorrowedDate: Date
        Collumn gets added to store date for the bookborrowed.
    ReturnDate: Date
        Collumn is added to store the terun dates of the books been 
        borrowed already.
    
    Methods
    -------

    __init__(LmsUserID, BookID, Status , BorrowedDate, ReturnedDate,BookBorrowedID = None)
        This method initializes the values for the BookBorrowed table.

    
    
    
    """
    __tablename__ = "BookBorrowed"
    BookBorrowedID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    LmsUserID = db.Column(db.Integer)
    BookID = db.Column(db.Integer)
    Status = db.Column(db.DateTime)
    BorrowedDate = db.Column(db.DateTime)
    ReturnedDate = db.Column(db.DateTime)
    EventID = db.Column(db.DateTime)
    # Username = db.Column(db.String(256), unique = True)

    def __init__(self,LmsUserID, BookID, Status , BorrowedDate, ReturnedDate,BookBorrowedID = None):
        self.LmsUserID = LmsUserID
        self.BookID = BookID
        self.Status = Status
        self.BorrowedDate = BorrowedDate
        self.ReturnedDate = ReturnedDate
        self.BookBorrowedID  = BookBorrowedID 

class BorrowedSchema(ma.Schema):
    """
    This calss takes in the fields for each books using nested class named meta
    and calling the borrschema object the Borrowedbook information is saved. 

    Mthods
    ------

    getBook()
        Api calls for getting all the books out to show as json data.
    getBookbyID(id)
        Api calls to get book by particular book id.
    addBook()
        Its a post method for post api call to add a book in the database using 
        api post call method. 
    bookDelete(id)
        Delate api call method for api to delate a book by its provided 
        book id. 
    """
    # Reference: https://github.com/marshmallow-code/marshmallow/issues/377#issuecomment-261628415
    def __init__(self, strict = True, **kwargs):
        super().__init__(strict = strict, **kwargs)
    
    class Meta:
        # Fields to expose.
        fields = ("BookBorrowedID", "LmsUserID","BookID", "Status","BorrowedDate","ReturnedDate","EventID")

borrSchema = BorrowedSchema()
borrsSchema = BorrowedSchema(many = True)

# Endpoint to show all Books.
@api.route("/api/book", methods = ["GET"])
def getBook():
    book = Book.query.all()
    result = booksSchema.dump(book)

    return jsonify(result.data)

#Endpoint to get book by id
@api.route("/api/book/<id>", methods = ["GET"])
def getBookbyID(id):
    book = Book.query.get(id)

    return bookSchema.jsonify(book)

# Endpoint to create new book.
@api.route("/api/book", methods = ["POST"])
def addBook():
    author = request.json["Author"]
    date = request.json["PublishedDate"]
    title = request.json["Title"]

    newBook = Book(Author = author, Title = title, PublishedDate = date)

    db.session.add(newBook)
    db.session.commit()

    return bookSchema.jsonify(newBook)
# Endpoint to create new book.
@api.route("/api/book/<id>", methods = ["DELETE"])
def bookDelete(id):
    book = Book.query.get(id)
    BookBorrow.query.filter(BookBorrow.BookID == id).delete()
    print(book)

    db.session.delete(book)
    db.session.commit()

    return bookSchema.jsonify(book)