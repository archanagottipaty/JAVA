from flask import Flask, render_template
from flask import request
from flask import redirect
from flask_bcrypt import Bcrypt  
from mysqlconnection import connectToMySQL
app = Flask(__name__)     
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument
print("*******************************printing app")
print(app)
@app.route('/')
def create():
    # include some logic to validate user input before adding them to the database!
    # create the hash

    pw_hash = bcrypt.generate_password_hash('mypassword')  
    print(pw_hash)  
    print("*******************************printing app")
    print(app)
    print("***************************printing locals")
    print(locals())
    print("*****************************ended printing locals")
    # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'
    # be sure you set up your database so it can store password hashes this long (60 characters)
    mysql = connectToMySQL("Users")
    query = "INSERT INTO Users (username, password) VALUES (%(username)s, %(password_hash)s);"
    # put the pw_hash in our data dictionary, NOT the password the user provided
    data = { "username" :"archanag",
             "password_hash" : pw_hash }
    mysql.query_db(query, data)
    # never render on a post, always redirect!
    print("***************************printing locals")
    print(locals())
    print("*****************************ended printing locals")

    
    return render_template("index.html", pw=pw_hash, rf='archanag')
if __name__ == "__main__":
    app.run(debug=True)