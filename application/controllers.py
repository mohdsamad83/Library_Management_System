from flask import Flask, render_template, redirect, request
from flask import current_app as app
from .models import *


@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        this_username = request.form.get("username")
        this_password = request.form.get("password")
        this_user = User.query.filter_by(username=this_username, password=this_password).first()
        if this_user:
            if this_user.type == "admin":
                # print("Admin logged in")
                return render_template("admin_dashboard.html", this_user=this_user)
            else:
                return render_template("user_dashboard.html", this_user=this_user)
                # print("General user logged in")
        else:
            return "Invalid credentials"
    return render_template("login.html")

@app.route("/register",methods = ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        this_email = request.form.get("email")
        this_username = request.form.get("username")
        this_password = request.form.get("password")
        this_user = User.query.filter_by(email=this_email, username=this_username, password=this_password).first()
        if this_user:
            return "User already exists. Please login." 
        elif not this_email or not this_username or not this_password:
            return "Please fill all the fields." 
        else:
            user = User(email=this_email, username=this_username, password=this_password)
            db.session.add(user)
            db.session.commit()
        return render_template("login.html")
    


@app.route("/admin_dashboard",methods = ["GET","POST"])
def admin_dashboard():
    if request.method == "GET":
        return render_template("admin_dashboard.html")
    if request.method == "POST":
        return render_template("admin_dashboard.html")
    
        
@app.route("/create_eb.html", methods=["GET","POST"])
def create_eb():
    if request.method == "GET":
        return render_template("create_eb.html")
    if request.method == "POST":
        b_name = request.form.get("b_name")
        author = request.form.get("author")
        b_url = request.form.get("b_url")
        ebook = Ebook(b_name = b_name, author = author,b_url = b_url)
        db.session.add(ebook)
        db.session.commit()
    return render_template("admin_dashboard.html")




@app.route("/user_dashboard",methods = ["GET","POST"])
def user_dashboard():

    return render_template("user_dashboard.html")