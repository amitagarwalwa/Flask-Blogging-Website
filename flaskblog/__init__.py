from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app=Flask(__name__)
# import secrets
# secrets.token_hex(16)
app.config['SECRET_KEY']='4de38aa14fdc24d2504f288e21c7e8b2'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
#call instance of db
db=SQLAlchemy(app)
bcrypt=Bcrypt()

from flaskblog import routes

