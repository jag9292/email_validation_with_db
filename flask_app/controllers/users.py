from flask import render_template,redirect,request,flash,session
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User


@app.route('/')
def email():
    
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def enter_email():
    if not User.validate_email(request.form):
        return redirect('/')

    User.add(request.form)
    return redirect('/success')

@app.route("/success")
def success():
    mysql = connectToMySQL('email_validation')
    users = mysql.query_db('SELECT * FROM users;')
    return render_template("success.html", all_users = users)

@app.route('/delete/<id>')
def delete_user(id):
    data = {
        "id" : int(id)
    }
    User.delete(data)
    return redirect("/success")
