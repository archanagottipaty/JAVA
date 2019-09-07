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
    mysql = connectToMySQL("EXAM")
    users = mysql.query_db("SELECT * FROM Users where first='krishna';")
    print(users)
    return render_template("index.html", all_users = users)
    

if __name__ == "__main__":
    app.run(debug=True)
