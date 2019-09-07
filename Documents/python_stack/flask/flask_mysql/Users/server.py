from flask import Flask, render_template, flash,request,redirect
from mysqlconnection import connectToMySQL# import the function that will return an instance of a connection
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
app = Flask(__name__)
app.secret_key="keep it secret"
@app.route('/users/new')
def index():
    #mysql = connectToMySQL('twitter')# call the function, passing in the name of our db
    #  pets = mysql.query_db('SELECT * FROM Users;')  
    # call the query_db function, pass in the query as a string
    # print(pets)
    return render_template("index.html")
            
@app.route("/users/new", methods=["POST"])
def add_user_to_db():
    is_valid = True		# assume True
    if len(request.form['First Name']) < 1:
        flash("Please enter a first name")
        is_valid = False
    	# display validation error
    if len(request.form['Last Name']) < 1:
        flash("Please enter a last name")
        is_valid = False
    	# display validation error
    if len(request.form['Email']) < 2:
        #flash("Please enter an Email")
        is_valid = False
    	# display validation error
    
    if not is_valid:# if any of the fields switched our is_valid toggle to False
        return redirect('/users/new')   # redirect back to the method that displays the index page
    else:   # if is_valid is still True, all validation checks were passed
    	# add user to database
        # display success message
        # redirect to a method that displays a success page
        mysql = connectToMySQL("twitter")
        query = "INSERT INTO users (first_name, last_name,handle) VALUES ( %(fn)s, %(ln)s,%(em)s);"
        data = {
        "fn":request.form["First Name"],
        "ln":request.form["Last Name"],
        "em":request.form["Email"]
        }
        print("========================>>>>>")
        print(query)
        new_user_id = mysql.query_db(query,data)
        print(request.form)
        return redirect('/users/'+str(new_user_id))
    
    # query = INSERT INTO Users(first_name, last_name, Email, created_at, updated_at) 
    #                         VALUES (fn from form, ln from form, em from form, NOW(), NOW());

@app.route("/users/<id>")
def print_added_user(id):
    mysql = connectToMySQL("twitter")
    
    query = "SELECT * FROM Users WHERE id= %(thisid)s;"

    data = {
        "thisid":id
        }
    print(query)
    user=mysql.query_db(query,data)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(user)
    return render_template("one_user.html", user=user )

@app.route("/users/<id>/edit")
def edit_user(id):
    mysql = connectToMySQL("twitter")
    query = "SELECT * FROM  users WHERE id=%(thisid)s;"
    data = {
        "thisid":id
        }
    user=mysql.query_db(query,data)
    return render_template("edit_user.html", user=user)
    
@app.route("/users/<id>/edit", methods=["POST"])
def edit_user_post(id):
    mysql = connectToMySQL("twitter")
    query = "UPDATE users set first_name=%(fn)s, last_name=%(ln)s,handle=%(em)s; where id =%(id)s"
    data = {
        "fn":request.form["First Name"],
        "ln":request.form["Last Name"],
        "em":request.form["Email"]
    }
    user=mysql.query_db(query,data)
    # data = {
    #     "fn":request.form["First Name"],
    #     "ln":request.form["Last Name"],
    #     "em":request.form["E-mail"]
    # }
    return redirect("/users/"+str(id))

@app.route("/users")
def display_database():
    mysql = connectToMySQL("twitter")
    query = "Select * from users;"
    data = {
    }
    user=mysql.query_db(query,data)
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print(user)
    # data = {
    #     "fn":request.form["First Name"],
    #     "ln":request.form["Last Name"],
    #     "em":request.form["E-mail"]
    # }
    return render_template("readall.html", user=user)


# @app.route("/users/")
# def edit_user(id):
#     mysql = connectToMySQL("twitter")
#     query = "SELECT * FROM  users WHERE id=%(thisid)s;"
#     data = {
#         "thisid":id
#         }
    
#     user=mysql.query_db(query,data)
#     # data = {
#     #     "fn":request.form["First Name"],
#     #     "ln":request.form["Last Name"],
#     #     "em":request.form["Email"]
#     # }
#     return render_template("edit_user.html", id=id, user=user)

if __name__ == "__main__":
    app.run(debug=True)