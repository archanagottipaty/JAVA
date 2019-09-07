from flask import Flask, render_template, flash, session
from flask import request
from flask import redirect
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def index_form():
    is_valid=True
    if len(request.form['name']) == 0:
        is_valid = False
        print("is_valid", is_valid)
        flash("Please enter a movie title:")
        return redirect("/")
    session['movie']=request.form['name']
    print("Session['movie']", session['movie'])
    return redirect("/theaters")
    

@app.route('/theaters')
def theaters():
    mysql = connectToMySQL("myproject")
    query ="select Movies.movieid from Movies where Movies.name=%(name)s"
    data={"name" : session['movie']}
    movie_id = mysql.query_db(query, data)
    print("Movie id is:", movie_id)
    print("Length of movie is", len(movie_id))
    if len(movie_id)==0:
        flash("This movie is not playing anywhere.")
        return redirect('/')

    mysql = connectToMySQL("myproject")
    query = "select Theaters.Name from Movies JOIN Theaters_has_Movies ON Movies.movieid = Theaters_has_Movies.Movies_movieid JOIN Theaters ON Theaters_has_Movies.Theaters_theaterid = Theaters.theaterid where Movies.movieid = (%(id)s)"
    # # put the pw_hash in our data dictionary, NOT the password the user provided
    data = { "id" : movie_id[0]['movieid']}
    print("data:", data)
    theaters = mysql.query_db(query, data)
    print("MOVIE QUERY IS: ",query)
    print("query result: ", theaters)
    return render_template("theater.html", theaters=theaters )

# @app.route("/edittrip", methods = ['POST'])
# def edittrip2():
#     is_valid=True
#     if len(request.form['destination'])<4:
#         is_valid = False
#         print("is_valid", is_valid)
#         flash("Please enter destination value that is longer")
#     if len(request.form['plan'])== 0:
#         flash("Please enter a value for Plan")
#         is_valid=False
#     if is_valid == False:
#         print("AM I HERE YET?")
#         return render_template("edittrip.html")

#     mysql = connectToMySQL("TRIPBUDDY2")
#     query = "select * from Trips where tripsid = (%(id)s) "
#     # # put the pw_hash in our data dictionary, NOT the password the user provided
#     data = { "id" : id}
#     trips = mysql.query_db(query, data)


#     mysql = connectToMySQL("TRIPBUDDY2")
#     query = "insert into Trips VALUES (NULL, %(destination)s, %(start)s, %(end)s, %(plan)s, NOW(), NOW(),%(session)s)"
#     data = {
#         "destination": request.form["destination"],
#         "start": request.form["start"],
#         "end": request.form["end"],
#         "plan": request.form["plan"],
#         "session": session['id']
#     }
#     insert_trip = mysql.query_db(query, data)


#     mysql = connectToMySQL("TRIPBUDDY2")
#     query = "DELETE FROM TRIPS WHERE  tripsid=%(id)s"
#     data = {
#         "id": id}
#     remove_trip = mysql.query_db(query, data)


#     mysql = connectToMySQL("TRIPBUDDY2")
#     query = "UPDATE Trips SET destination = %(destination)s, start = %(start)s, end =%(end)s, plan = %(plan)s WHERE tripsid=%(id)s"
#     data = {
#         "destination": request.form["destination"],
#         "start": request.form["start"],
#         "end": request.form["end"],
#         "plan": request.form["plan"],
#         "id": session["tripid"]}
#     edit_trip = mysql.query_db(query, data)
#     print("Edit_trip", edit_trip)

#     mysql = connectToMySQL("TRIPBUDDY2")
#         # query = "INSERT INTO Registered_Users (username, password) VALUES (%(username)s, %(password_hash)s);"
#         # # put the pw_hash in our data dictionary, NOT the password the user provided
#         # data = { "username" : request.form['username'],
#         #      "password_hash" : pw_hash }
#         # mysql.query_db(query, data)
#         print("+++++++++++++++++++Before INSERT")
#         data = {"first" : request.form['first'],
#                 "last" : request.form['last'],
#                 "email" : request.form['email'],
#                 "password" : request.form['password']}
#         query = "INSERT INTO Users VALUES (NULL, %(first)s, %(last)s, %(email)s, %(password)s,NOW(), NOW())"
#         print(query)
#         new_registereduser_id = mysql.query_db(query,data)

#     return redirect("/dashboard")

@app.route('/logout')
def logout():
    print("XXXXXXXXXXXXXXXXXXX")
    session.clear()
    print("Inside logout")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
