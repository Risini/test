from flask import Flask, render_template, request
from flask_mysqldb import MySQL

# render template is used to render html files.

# initiate an object app for this flask class to pass the current module __name__
app = Flask(__name__)

# configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Risini@1999'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('home.html')


# will search for a html file that called through render_template function in the folder from the root of the project


# call the decorator route through the object or variable app and the request is been made
@app.route('/form_tabledata', methods=['GET', 'POST'])
def login():
    # we can check if the form is a get or post request by calling this method
    if request.method == 'POST':

        # fetch from data
        name = request.form['name']
        password = request.form['password']

        # password is a string. it need to be a tuple because the data fetching from the database is in a tuple.
        password_to_tuple = (password,)

        # creating a cursor
        log_cursor = mysql.connection.cursor()
        # sql query (in a way preventing from sql injection)
        log_cursor.execute("""SELECT password FROM passwordtable WHERE name=%(name)s AND password = %(password)s""",
                           {'name': name, 'password': password})
        # fetching one data to a variable called db_password. and it is a tuple
        db_password = log_cursor.fetchone()
        mysql.connection.commit()
        log_cursor.close()

        # def data_list():
        #     list_cursor = mysql.connection.cursor()
        #     list_cursor.execute("SELECT (name, dob, age, authority, password) FROM passwordtable")
        #     result = list_cursor.fetchall()
        #     mysql.connection.commit()
        #     list_cursor.close()
        #     return result
        #
        # res = data_list()

        # check if the password we are getting from the html file (password_to_tuple) is equal to password getting
        # from the database (db_password)
        if db_password == password_to_tuple:
            return render_template('tabledata.html')#, result=res)
        else:
            return 'failure'


@app.route('/form_insertdata', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        # fetch from data
        user_details = request.form
        name = user_details['name']
        dob = user_details['dob']
        age = user_details['age']
        authority = user_details['authority']
        password = user_details['password']

        # creating a cursor
        insert_cursor = mysql.connection.cursor()
        # sql query
        insert_cursor.execute(
            "INSERT INTO passwordtable (name, dob, age, authority, password) VALUES(%(name)s, %(dob)s, %(age)s, "
            "%(authority)s, %(password)s)",
            {'name': name, 'dob': dob, 'age': age, 'authority': authority, 'password': password})
        # cur.execute("DELETE FROM appdata WHERE name='Hasi'")
        mysql.connection.commit()
        insert_cursor.close()
        return 'success'


# if the current module is running this __name__ attribute will hold the value in main
if __name__ == '__main__':
    app.run(debug=False)
# debug = true will make sure that any change we make will immediately update to the web browser
