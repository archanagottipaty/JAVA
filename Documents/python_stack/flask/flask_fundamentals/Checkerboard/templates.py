from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/play/<x>/<color>')                           
def hello_world(x, color):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', times = int(x), color = color)  
    
if __name__=="__main__":
    app.run(debug=True)                   

# @app.route('/repeat/<num>/<text>')
# def repeat(num,text):
	#print(int("num"))

	# mynum = int(num)
	#for i in range(mynum):
	# mystring = (text + "<br>") * int(num) 
	# return mystring