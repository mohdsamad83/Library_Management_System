from .database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(),unique = True, nullable = False)
    username = db.Column(db.String(), unique = True, nullable = False)
    password = db.Column (db.String(), nullable = False)
    type = db.Column (db.String(),default ="general")
    ebooks = db.relationship('Ebook', backref = 'bearer')


class Ebook(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    b_name = db.Column(db.String(), nullable = False)
    author = db.Column(db.String(), nullable = False)
    b_url = db.Column(db.String(), nullable = True)
    status = db.Column(db.String(), default = "Available")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = True)

