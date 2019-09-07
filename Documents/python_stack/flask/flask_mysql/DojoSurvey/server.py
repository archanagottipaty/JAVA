from flask import Flask, render_template, flash, session
from flask import request
from flask import redirect
from mysqlconnection import connectToMySQL 
import re
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/person/<id>')
def person(id):
        print("I am inside person route")
        print("Id is: ", id)
        return render_template('index.html')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods = ["POST"])
def results():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    yname = request.form['yname']
    location = request.form['location']
    language = request.form['language']
    mycomments = request.form['mycomments']
    print(request.form['yname'])
    print(request.form['location'])
    print(request.form['language'])
    print(request.form['mycomments'])

    mysql = connectToMySQL("DojoSurvey")
    data = {"yname" : request.form['yname'],
                "location" : request.form['location'],
                "language" : request.form['language'],
                "mycomments" : request.form['mycomments']}
    query = "INSERT INTO DojoSurvey VALUES (NULL, %(yname)s, %(location)s, %(language)s, %(mycomments)s, NOW(), NOW())"
    print(query)
        #new_registereduser_id = mysql.query_db(" SELECT * FROM Registered_Users")
    new_registereduser_id = mysql.query_db(query,data)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(new_registereduser_id)
    # # put the pw_hash in our data dictionary, NOT the password the user provided

    return render_template("result.html", yname =yname, location=location, language=language,mycomments=mycomments)

    
    
if __name__ == "__main__":
    app.run(debug=True)