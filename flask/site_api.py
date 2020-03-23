from flask import Flask, url_for, Blueprint, request, jsonify, render_template,Flask, flash, redirect, render_template, request, session, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json

"""
This site_api class inegrates the api with the site view
and helps geeting, posting and delating functions through api calls wiythin in 
the cloud thus acts as the client for the site.

Methods
-------

index()
    it srats up based on the index template.
    It starts as landing site with basic functional
    features in the site.

do_admin_login()
    Admin login functionalities through api get and post requests
    as user types in user name and password thus it posts the request to 
    the api for login and the api checks the user name and password with the 
    existing database thus it gets api results.
    
dashboard()
    This method opens app the dashbord site view based on rendering template
    dashboard.html.
report()
    This method helps getting the response ass all the books in the database 
    as rendered site as report.html.
addmenu()
    Allows user to type in book information through the site to add a book
    through the api calls to the cloud database.
delete()
    Using restful api calls this method allows user to delate 
    a book from cloud database based on users action on the site. 
"""

app = Flask(__name__)
app.secret_key = 'super secret key'

# Client webpage.
@app.route("/")
def index():
    
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def do_admin_login():
    
    if request.form['password'] == 'hghar' and request.form['username'] == 'jaqen':
        
        session['logged_in'] = True
        return redirect(url_for('dashboard'))
    else:
        flash('wrong password!')
        return redirect(url_for('index'))

@app.route('/dashboard',  methods = ['GET', 'POST'])
def dashboard():
	return render_template("dashboard.html")

@app.route('/getreport',  methods = ['GET', 'POST'])
def report():
    # Use REST API.
    response = requests.get("http://localhost:5000/api/book")
    data = json.loads(response.text)

    return render_template("getreport.html", book = data)

@app.route('/addbooks',  methods = ['GET', 'POST'])
def addmenu():
    # Use REST API.
    return render_template("addbook.html")

@app.route('/removebooks',  methods = ['GET', 'POST'])
def delete():
    # Use REST API.
    print("Hi im deleting")
    return render_template("deletebook.html")

@app.route('/added',  methods = ['GET','POST'])
def bookadd():
    # Use REST API.
    for x in range(int(request.form['Number of Copies'])):
            data = {"Author": request.form['Author'],
                    "PublishedDate":request.form['PublishedDate'], 
                    "Title":request.form['Title']
                    } 
            headers = {
                'Content-Type': 'application/json',
            }
            # sending post request and saving response as response object 
            requests.post(url = "http://localhost:5000/api/book", headers=headers ,data = json.dumps(data)) 
    
    return redirect(url_for('dashboard'))

@app.route('/delete',  methods = ['POST'])
def bookdelete():
    # Use REST API.
    
    bookid = request.form['BookID']
# sending post request and saving response as response object 
    e = requests.delete(url = "http://localhost:5000/api/book/"+bookid) 
    print(e)
    
    return redirect(url_for('dashboard'))

@app.route('/visualization',  methods = ['GET', 'POST'])
def visual():
    # Use REST API.
    return render_template("visualization.html")



if __name__ == "__main__":
    

    app.run(host = "0.0.0.0", port ="5050",debug = False)

