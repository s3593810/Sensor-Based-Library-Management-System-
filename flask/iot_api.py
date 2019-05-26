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