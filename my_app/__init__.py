from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#Initializes App and uses working directory's name as app name 
app = Flask(__name__)

#Initializes SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
 
from my_app.baseline.views import baseline
app.register_blueprint(baseline)
 
#Creates Database
db.create_all()