#Used to Create Model for BasePerson
#db was initialized in  my_app/init.py

from my_app import db
 
class BasePerson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(3))
 
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
 
    def __repr__(self):
        return '<Person %d>' % self.id