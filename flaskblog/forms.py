from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SearchField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,regexp,EqualTo

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(max=20,min=2)])
    email=StringField('Email',validators=[DataRequired()])
    password=StringField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])

    submit=SubmitField('Sign Up')


    


class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    password=StringField('Password',validators=[DataRequired()])

    submit=SubmitField('Login')   

 
       
