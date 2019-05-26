from flask import Flask, url_for, Blueprint, request, jsonify, render_template,Flask, flash, redirect, render_template, request, session, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json

app = Flask(__name__)
app.secret_key = 'super secret key'

# Client webpage.
@app.route("/")
def index():
    print("test1")
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def do_admin_login():
    print("tada")
    if request.form['password'] == 'hghar' and request.form['username'] == 'jaqen':
        print("true")
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
    print("Am i working ???")
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

