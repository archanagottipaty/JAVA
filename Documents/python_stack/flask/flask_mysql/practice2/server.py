from flask import Flask, render_template, flash, session
from flask import request
from flask import redirect
import re

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def start():
    print("{{{{{{{")
    print(request.form)
    if len(request.form["first"]) <2 :
        flash("Something was wrong!", error)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)