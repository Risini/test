from flask import Flask, render_template, request
from flask_mysqldb import MySQL
# render template is used to render html files.

# initiate an object app for this flask class to pass the current module __name__
app = Flask(__name__)

#configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Risini@1999'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

# call the decorator route through the object or variable app and the request is been made
@app.route('/', methods = ['GET', 'POST'])
def index():
	# we can check if the form is a get or post request by calling this method
	if request.method == 'POST':
		# fetch from data
		userDetails = request.form
		name = userDetails['name']
		dob = userDetails['dob']
		age = userDetails['age']
		authority = userDetails['authority']
		password = userDetails['password']

		# creating a cursor
		cur = mysql.connection.cursor()
		# sql query 
		cur.execute("INSERT INTO passwordtable (name, dob, age, authority, password) VALUES(%s, %s, %s, %s, %s)",(name, dob, age, authority, password))
		# cur.execute("DELETE FROM appdata WHERE name='Hasi'")
		mysql.connection.commit()
		cur.close()
		return 'success'

	# will search for a html file that called through render_template function in the folder from the root of the project	
	return render_template('index.html')

# if the current module is running this __name__ attribute will hold the value in main
if __name__ == '__main__':
	app.run(debug = True)
	# debug = true will make sure that any change we make will imidiately update to the web browser