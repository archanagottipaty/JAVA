from flask import Flask, render_template
from flask import request
from flask import redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route('/copy')
def index():
    mysql = connectToMySQL('CPlusRPets')# call the function, passing in the name of our db
    pets = mysql.query_db('SELECT * FROM pets;')  # call the query_db function, pass in the query as a string
    print(pets)
    return render_template("index.html", all_pets=pets)
            
@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    mysql = connectToMySQL("CPlusRPets")
    query = "INSERT INTO pets (name, type ) VALUES ( %(ln)s, %(occup)s);"
    data = {
       
        "ln":request.form["Pet"],
        "occup":request.form["Type"]
    }
    new_pet_id = mysql.query_db(query,data)
    db = connectToMySQL('CPlusRPets')
    return redirect("/copy")
    print(request.form)
    # QUERY: INSERT INTO first_flask (first_name, last_name, occupation, created_at, updated_at) 
    #                         VALUES (fname from form, lname from form, occupation from form, NOW(), NOW());
if __name__ == "__main__":
    app.run(debug=True)