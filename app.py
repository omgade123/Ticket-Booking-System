from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'iitpawai07'
app.config['MYSQL_DB'] = 'form'
mysql = MySQL(app)


@app.route('/actionname', methods=['GET', 'POST'])
def xyz():
    if request.method == 'POST':
        try:
            Name = request.form['Name']
            Number = int(request.form['Number'])  # Convert to int
            Email = request.form['Email']

            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO data(Name, Number , Email) VALUES(%s, %s, %s)",
                (Name, Number, Email))
            mysql.connection.commit()
            cur.close()
            return "INSERTED SUCCESSFULLY !!"
        except Exception as e:
            # Handle the error, log it, and return an error message
            error_message = f"Error: {str(e)}"
            return error_message
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)