from flask import Flask, render_template, redirect, request, url_for
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
                # return render_template("admin_dashboard.html", user=this_user)
                return redirect(url_for("admin_dashboard", user = this_user, user_id = this_user.id))
            else:
                return redirect(url_for("user_dashboard", user_id = this_user.id))
                # print("General user logged in")
                # print(this_user.id)
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

@app.route("/admin_dashboard/<int:user_id>", methods=["GET"])
def admin_dashboard(user_id):
    this_user = User.query.filter_by(id=int(user_id)).first()
    e_books = Ebook.query.filter_by(status="Requested").all()
    A_books = Ebook.query.filter_by(status="Available").all()
    G_books = Ebook.query.filter_by(status="Granted").all()
    e_users = User.query.filter_by(type="general").all()
    Etotal_users = Ebook.query.all()
    return render_template("admin_dashboard.html", user=this_user, admin_total_ebooks=Etotal_users, admin_books=e_books,admin_users = e_users, admin_a_book=A_books,admin_g_book = G_books)

@app.route("/grant_permission/<int:user_id>/<int:book_id>/<int:customer_user_id>",methods=["GET"])
def grant_permission(user_id,book_id,customer_user_id):
    book = Ebook.query.get(book_id)
    book.status = "Granted"
    book.user_id = customer_user_id
    db.session.commit()
    return redirect(url_for("admin_dashboard", user_id=user_id))



@app.route("/create_eb", methods=["GET","POST"])
def create_eb():
    this_user = User.query.filter_by(type = "admin").first()
    if request.method == "POST":
        b_name = request.form.get("b_name")
        author = request.form.get("author")
        b_url = request.form.get("b_url")
        ebook = Ebook(b_name = b_name, author = author,b_url = b_url)
        db.session.add(ebook)
        db.session.commit()
        return redirect(url_for("admin_dashboard", user = this_user, user_id = this_user.id))
    return render_template("create_eb.html")
    


@app.route("/user_dashboard/<int:user_id>", methods=["GET"])
def user_dashboard(user_id):
    this_user = User.query.filter_by(id=int(user_id)).first()
    e_books = Ebook.query.filter_by(status="Available").all()
    g_books = Ebook.query.filter_by(status="Granted",user_id = int(user_id)).all()
    
    # e_books = Ebook.query.filter_by(status="Requested").all()
    return render_template("user_dashboard.html", user=this_user, e_books=e_books, g_books=g_books)

@app.route("/request/<int:user_id>/<int:book_id>",methods=["GET"])
def request_book(user_id,book_id):
    book = Ebook.query.get(book_id)
    book.status = "Requested"
    book.user_id = user_id
    db.session.commit()
    return redirect(url_for("user_dashboard", user_id=user_id))

@app.route("/return_granted/<int:user_id>/<int:book_id>",methods=["GET"])
def return_granted(user_id,book_id):
    book = Ebook.query.get(book_id)
    book.status = "Available"
    book.user_id = "null"
    db.session.commit()
    return redirect(url_for("user_dashboard", user_id=user_id))




