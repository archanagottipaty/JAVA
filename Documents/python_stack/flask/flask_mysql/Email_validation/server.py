from flask import Flask, render_template, flash,request,redirect
import re	# the regex module
from mysqlconnection import connectToMySQL# import the function that will return an instance of a connection

app = Flask(__name__)
app.secret_key="keep it secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
    return render_template('index.html', error=error)

@app.route('/', methods=["POST"])
def entered_email():
    mysql = connectToMySQL("twitter")
    query = "INSERT INTO users (first_name, last_name,handle) VALUES ( %(em)s);"
    data = {
        "em":request.form["Email"]
        }    
    # create a regular expression object that we'll use later   
       
@app.route('/process', methods=['POST'])
def submit():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
    if not EMAIL_REGEX.match(request.form['Email']):# test whether a field matches the pattern
        flash("Invalid email address!")
        return redirect('/before_process')
    print("========================>>>>>")
    # print(query)
    # new_user_id = mysql.query_db(query,data)
    print(request.form)
    return redirect("/success")

@app.route('/before_process')
def before_process():
    return render_template("index.html")

@app.route('/success')
def success():
    mysql = connectToMySQL("twitter")
    query = "select * from Emails;"
    data = {
        }
    print("========================>>>>>")
    print(query)
    all = mysql.query_db(query,data)
    print(request.form)
    return render_template("success.html",all=all )

if __name__ == "__main__":
    app.run(debug=True)
