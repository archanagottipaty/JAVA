from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/') 
def hello_world():
    return 'Hello World!'


@app.route('/say/<something>') 
def hello(something):
	return "Hello:" + something

@app.route('/dojo')
def success():
	print('test')
	return ('Dojo!') 


@app.route('/repeat/<num>/<text>')
def repeat(num,text):
	#print(int("num"))

	mynum = int(num)
	#for i in range(mynum):
	mystring = (text + "<br>") * int(num) 
	return mystring

@app.route('/users/<username>/<id>')  
def show_user_profile(username, id):
	return "username: " + username + ", id: " + id

if __name__=="__main__":  
	app.run(debug=True) 
