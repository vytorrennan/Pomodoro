from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path

basedir = path.abspath(path.dirname(__file__))


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(basedir, "database.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Student {self.email}>"


@app.route("/")
def pomodoro():
    return render_template("pomodoro.html")

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        if request.form.get("btnRegister") == "Register":
            newUser = Student(email=request.form["emailRegister"], password=request.form["passwordRegister"])
            print(newUser)
            print(newUser.id)
            print(newUser.email)
            print(newUser.password)
        elif request.form.get("btnLogin") == "Login":
            print("Login")
        
    return render_template("account.html")

if __name__ == "__main__":
    app.run(debug=True)
