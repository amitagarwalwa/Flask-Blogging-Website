
from flask import render_template,url_for,flash,redirect
from flaskblog.forms import RegistrationForm,LoginForm     # own module
from flaskblog import app,db,bcrypt
from flaskblog.models import User,Post
from flask_login import current_user,login_user  

posts=[
    {
        'author':'Biksah',
        'title':'blog post 1',  
        'content':'Movie Recommend',
        'date_posted':'April 30, 2022'
    },
    {
        'author':'Rakesh',
        'title':'blog post 2',
        'content':'Become a CA',
        'date_posted':'May 20, 2023'
    },
]

with app.app_context():
        db.create_all()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)



@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()    #init instance 
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account is created! you can login in now !','success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)


# https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Flask_Blog/06-Login-Auth/flaskblog/templates/layout.html

@app.route('/login', methods=['GET','POST'])
def login():
    
    form=LoginForm()    #init instance 
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password':
            flash('You have been logged in !','success')
            return redirect(url_for('home'))
        else:         
            flash('Login Unsucessful.Please check username and password','danger')
    return render_template('login.html',title='Login',form=form)