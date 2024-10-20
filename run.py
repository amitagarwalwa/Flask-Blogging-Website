# from flask import Flask,render_template,url_for,flash,redirect
# from flaskblog.forms import RegistrationForm,LoginForm     # own module
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# app=Flask(__name__)
# # import secrets
# # secrets.token_hex(16)
# app.config['SECRET_KEY']='4de38aa14fdc24d2504f288e21c7e8b2'
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
# #call instance of db
# db=SQLAlchemy(app)


# #create a model
# class User(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     username=db.Column(db.String(20),unique_key=True ,nullable=False)
#     email=db.Column(db.String(120),unique_key=True ,nullable=False) 
#     image_file=db.Column(db.String(20),nullable=False ,default='defaulte.jpg')
#     password=db.Column(db.String(60),nullable=False)
#     posts=db.relationship('Post',backref='author',lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}','{self.email}','{self.image_file}')"
    
# #2nd table
# class Post(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     title=db.Column(db.String(100) ,nullable=False)
#     date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow) 
#     content=db.Column(db.Text,nullable=False)
#     user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)     #foreign key

#     def __repr__(self):
#         return f"User('{self.title}','{self.date_posted}')"

# posts=[
#     {
#         'author':'Biksah',
#         'title':'blog post 1',
#         'content':'Movie Recommend',
#         'date_posted':'April 30, 2022'
#     },
#     {
#         'author':'Rakesh',
#         'title':'blog post 2',
#         'content':'Become a CA',
#         'date_posted':'May 20, 2023'
#     },
# ]

# @app.route('/')
# @app.route('/home')
# def home():
#     return render_template('home.html',posts=posts)



# @app.route('/about')
# def about():
#     return render_template('about.html',title='About')

# @app.route('/register',methods=['GET','POST'])
# def register():
#     form=RegistrationForm()    #init instance 
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!','success')
#         redirect(url_for('home'))
#     return render_template('register.html',title='Register',form=form)

# @app.route('/login', methods=['GET','POST'])
# def login():
#     form=LoginForm()    #init instance 
#     if form.validate_on_submit():
#         if form.email.data=='admin@blog.com' and form.password.data=='password':
#             flash('You have been logged in !','success')
#             redirect(url_for('home'))
#         else:
#             flash('Login Unsucessful.Please check username and password','danger')
#     return render_template('login.html',title='Login',form=form)

from flaskblog import app
if __name__=="__main__":
    app.run(debug=True,port=3999)

      
# https://www.youtube.com/watch?v=CSHx6eCkmv0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=6&ab_channel=CoreySchafer
