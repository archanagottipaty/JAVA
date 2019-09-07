from flask import Flask, render_template,session
from flask import request
from flask import redirect
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'mycounter' in session:
        print('key exists!')
        session['mycounter'] += 1
    else:
        print("key 'mycounter' does NOT exist")
        session['mycounter'] = 0
    
    return render_template("index.html")

@app.route('/destroy_session')
def show_route():
    # session.clear()		# clears all keys
    session.pop('mycounter')	# clears a specific key
    return redirect('/')	

if __name__ == "__main__":
    app.run(debug=True)