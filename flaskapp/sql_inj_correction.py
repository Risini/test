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
def authority():
# we can check if the form is a get or post request by calling this method
	if request.method == 'POST':

		# fetch from data
		name = request.form['name']
		password = request.form['password']

		# password is a string. it need to be a tuple becouse the data fetching from the database is in a tuple.
		password_to_tuple = (password,)

		# creating a cursor
		cur = mysql.connection.cursor()
		# sql query (in a way preventing from sql injection)
		cur.execute("""SELECT password FROM passwordtable WHERE name=%(name)s AND password = %(password)s""" ,{'name':name, 'password':password})
		# fetching one data to a variable called db_password. and it is a tuple 
		db_password = cur.fetchone()

		# check if the pasword we are getting from the html file (password_to_tuple) is equal to password getting from the database (db_password)
		if db_password == password_to_tuple :
			return 'success'
		else:
			return 'failure'
			

		mysql.connection.commit()
		cur.close()

	# will search for a html file that called through render_template function in the folder from the root of the project
	return render_template('authority.html')

# if the current module is running this __name__ attribute will hold the value in main
if __name__ == '__main__':
	app.run(debug = True)
	# debug = true will make sure that any change we make will imidiately update to the web browser