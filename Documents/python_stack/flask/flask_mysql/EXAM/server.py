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
    
    print("I am in the GET method of /")
    return render_template("index.html")

@app.route('/register', methods=["POST"])
def register():
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
        mysql = connectToMySQL("EXAM")
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
        query = "INSERT INTO Users VALUES (NULL, %(first)s, %(last)s, %(email)s, %(password)s,NOW(), NOW())"
        print(query)
        new_registereduser_id = mysql.query_db(query,data)
        session['id'] =new_registereduser_id
        session['name']= request.form['first']
        print("____"*10)
        print(session['name'])  
    return redirect("/dashboard")
    

@app.route('/login', methods=["POST"])
def login():
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
        print("GOT THIS FAR AFTER VALIDATONS")
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
    
    mysql = connectToMySQL("EXAM")
    query = "select * from EXAM where Email = (%(email)s) "
    # # put the pw_hash in our data dictionary, NOT the password the user provided
    data = { "email" : request.form['email']}
    print("+++++++++++++++++++Printing data++++++++++++++++++++++")
    print(data)
    user_found = mysql.query_db(query, data)
    if user_found:
    # never render on a post, always redirect!  
        print("User_found" * 8)
        session['first'] = user_found[0]['first']
        session['id'] = user_found[0]['user_id']
        print("PPPP"*10)
        print(session['id'])
        return redirect("/dashboard")
    else: 
        return redirect("/")

@app.route("/dashboard")
def dashboard():
    saved_session = session['id']
    mysql = connectToMySQL("EXAM")
    query = "select  job_id,title,location, users_id from Jobs"
    # # put the pw_hash in our data dictionary, NOT the password the user provided
    print("%%"*20, session['id'])
    data = { "saved_session" : session['id']}
    jobs_found = mysql.query_db(query, data)
    print("##" * 50)
    print(jobs_found)
    print("Inside dashbord")
    return render_template("dashboard.html", jobs=jobs_found)

@app.route('/viewjob/')
def viewjob():
    mysql = connectToMySQL("EXAM")
    query = "SELECT * FROM Jobs WHERE job_id = %(jobid)s"
    data = { 
    "jobid": session["job_id"]}
    query_result = mysql.query_db(query,data)
    print("query_result:", query_result)
    print("Inside viewjob")
    return render_template("viewjob.html", query_result= query_result)


@app.route('/newjob')
def newjob():
    print("XXXXXXXXXXXXXXXXXXX")
    print("Inside newjob")
    return render_template("new.html")

@app.route('/editjob/<id>')
def editjob(id):
    session["job_id"]= id
    print("XXXXXXXXXXXXXXXXXXX")
    print("Inside editjob")
    return render_template("editjob.html")

@app.route('/logout')
def logout():
    print("XXXXXXXXXXXXXXXXXXX")
    session.clear()
    print("Inside logout")
    return redirect("/")

@app.route('/remove')
def remove():
    print("REMOVEREMOVEREMOVEREMOVEREMOVEREMOVEREMOVE")
    print("Inside remove")
    return redirect("/dashboard")

@app.route('/cancel')
def cancel():
    print("cancelcancelcancelcancelcancelcancelcancelcancelcancelcancelcancelcancel")
    print("Inside cancel")
    print (request.form)
    return redirect("/dashboard")

@app.route('/submit', methods= ['POST'])
def submit():
    print("submitsubmitsubmitsubmitsubmitsubmitsubmitsubmitsubmitsubmit")
    print("Inside submit")
    mysql = connectToMySQL("EXAM")
    query = "UPDATE Jobs SET title = %(title)s, location = %(location)s WHERE job_id = %(session)s"
    data = { "title" : request.form["title"],
    "description": request.form["description"],
    "location": request.form["location"],
    "session": session["job_id"]}
    query_result = mysql.query_db(query,data)
    print("+++"*30)
    print(query_result)
    return redirect("/dashboard")

@app.route('/submitnew', methods=["POST"])
def submitnew():
    
    print("Inside newInside submitnewInside submitnewInside submitnewInside submitnew")
    print("printing request.form:")
    print (request.form)
    is_valid = True
    print("Inside submitnewsubmitnew submit new")
    print(request.form)
    print()
    if request.form['location']== "" or request.form['title'] == "" or request.form["description"]=="":
        flash("Please enter a value for location")
        is_valid = False
    if len(request.form['title']) < 4 or len(request.form['description']) < 4 or len(request.form['location'])<4:
        flash("Please enter a longer title or description or location")
        is_valid = False
    if is_valid == False:
        return redirect("/newjob")
    
    mysql = connectToMySQL("EXAM")
    query = "INSERT INTO Jobs VALUES (NULL, %(title)s, %(location)s, NOW(), NOW(), %(users_id)s)"
    data = {
        "title": request.form['title'],
        "location": request.form['location'],
        "users_id": session['id']
    }
    returned_value = mysql.query_db(query,data)
    # query = "INSERT into Jobs VALUES  "
    # # # put the pw_hash in our data dictionary, NOT the password the user provided
    # print("%%"*20, session['id'])
    # saved_session = session['id']
    # data = { "user_id" : saved_session}
    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(debug=True)
