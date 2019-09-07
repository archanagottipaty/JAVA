from flask import Flask, render_template, flash, session
from flask import request
from flask import redirect
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def start():
    session.clear()
    print("I am in the GET method of /")
    return render_template("index.html")

@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/register', methods=["POST"])
def login():
    # include some logic to validate user input before adding them to the database!
    # create the hash
    # pw_hash = bcrypt.generate_password_hash(request.form['password'])  
    print("I am inside /login POST****************************************")
    # if len(request.form['first']) < 2:
    # 	flash("Please enter a firstname")
    # if len(request.form['last']) < 2:
    # 	flash("Please enter a lastname")
    # if len(request.form['email']) < 2:
    # 	flash("Please enter a email")
    # if len(request.form['password']) < 2:
    # 	flash("Please enter a password")
    # if (request.form['confirm_password'] != request.form['password']):
    # 	flash("Please enter a firstname")
    is_valid = True	
    if (request.form['first'] == ""):
        is_valid = False
        flash("First name not submitted")
    if len(request.form['first']) < 2:
        is_valid = False
        flash("Please enter a firstname longer than 2 chars")
    if (request.form['last'] == ""):
        is_valid = False
        flash("Last name not submitted")
    if not(request.form['first'].isalpha()):
        is_valid = False
        flash("Please enter only text")
    if len(request.form['last']) < 2:
        is_valid = False
        flash("Please enter a lastname longer than 2 chars")
    if not(request.form['last'].isalpha()):
        is_valid = False
        flash("Please enter only text")
    if len(request.form['first']) < 2:
        is_valid = False
        flash("Please enter a firstname longer than 2 chars")
    if request.form['email'].isalpha():
        is_valid = False
        flash("Please enter only text")
    if not EMAIL_REGEX.match(request.form['email']): 
        # test whether a field matches the pattern
        is_valid = False
        flash("Invalid email address!")
    if (request.form['password'] != request.form['confirm_password']):
        is_valid = False
        flash("Password and confirm_password do not match")
    if is_valid == False:
        return redirect("/")
    if is_valid == True:
        mysql = connectToMySQL("Registered_Users")
        # query = "INSERT INTO Registered_Users (username, password) VALUES (%(username)s, %(password_hash)s);"
        # # put the pw_hash in our data dictionary, NOT the password the user provided
        # data = { "username" : request.form['username'],
        #      "password_hash" : pw_hash }
        # mysql.query_db(query, data)
        print("+++++++++++++++++++Before INSERT")
        data = {"first" : request.form['first'],
                "last" : request.form['last'],
                "email" : request.form['email'],
                "password" : request.form['password']}
        query = "INSERT INTO Registered_Users VALUES (NULL, %(first)s, %(last)s, %(email)s, %(password)s)"
        print(query)
        #new_registereduser_id = mysql.query_db(" SELECT * FROM Registered_Users")
        new_registereduser_id = mysql.query_db(query,data)
        print("++++++++++++++++++++++++++print new_registereduser_id")
        print(new_registereduser_id)
        print("+++++++++++++++++++After INSERT")
        session['userid'] =new_registereduser_id
        session['first'] =request.form['first']
        session['last'] = request.form['last']
        
    return redirect("/success")
    
@app.route('/login', methods=["POST"])
def register():
    # include some logic to validate user input before adding them to the database!
    # create the hash
    # pw_hash = bcrypt.generate_password_hash(request.form['password'])  
    print("I am inside / POST****************************************")
    # if len(request.form['first']) < 2:
    # 	flash("Please enter a firstname")
    # if len(request.form['last']) < 2:
    # 	flash("Please enter a lastname")
    # if len(request.form['email']) < 2:
    # 	flash("Please enter a email")
    # if len(request.form['password']) < 2:
    # 	flash("Please enter a password")
    # if (request.form['confirm_password'] != request.form['password']):
    # 	flash("Please enter a firstname")

    # if not EMAIL_REGEX.match(request.form['email']): 
    #     # test whether a field matches the pattern
    #     is_valid = False
    #     flash("Invalid email address!")
    is_valid = True
    if not EMAIL_REGEX.match(request.form['email']): 
        flash("Invalid email address")
        is_valid = False
    if len(request.form['email']) < 2:
        flash("Please enter a Email")
        is_valid = False
    if len(request.form['password']) < 2:
        flash("Please enter a password")
        is_valid = False
    if is_valid == False:
        return redirect("/")

    # query = "INSERT INTO Registered_Users (username, password) VALUES (%(username)s, %(password_hash)s);"
        # # put the pw_hash in our data dictionary, NOT the password the user provided
        # data = { "username" : request.form['username'],
        #      "password_hash" : pw_hash }
        # mysql.query_db(query, data)
        # print("+++++++++++++++++++Before INSERT")
        # data = {"first" : request.form['first'],
        #         "last" : request.form['last'],
        #         "email" : request.form['email'],
        #         "password" : request.form['password']}
        # query = "INSERT INTO Registered_Users VALUES (NULL, %(first)s, %(last)s, %(email)s, %(password)s)"
        # print(query)
    
    mysql = connectToMySQL("Registered_Users")
    query = "select * from Registered_Users where Email = (%(email)s) "
    # # put the pw_hash in our data dictionary, NOT the password the user provided
    data = { "email" : request.form['email']}
    print("+++++++++++++++++++Printing data++++++++++++++++++++++")
    print(data)
    user_found = mysql.query_db(query, data)
    if user_found:
    # never render on a post, always redirect!  
        print("User_found" * 8)
        session['first'] = user_found[0]['first_name']
        session['last'] = user_found[0]['last_name']
        return redirect("/success")
    else: 
        return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)