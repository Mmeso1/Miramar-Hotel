from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, ValidationError
from wtforms.validators import InputRequired, Length, Email, EqualTo
from email_validator import validate_email, EmailNotValidError
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired("Username is required"),
        Length(min=2, max=20, message='Username must be between 2 and 20 characters')
    ])
    email = StringField('Email address', validators=[
        InputRequired("Email is required"),
        Email(message='Invalid email address format')
    ])
    password = PasswordField('Password', validators=[
        InputRequired('Password is required'),
        Length(min=6, message='Password must be at least 6 characters')
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        InputRequired('Please confirm your password'),
        EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Sign Up') 
    
    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError('That username is taken. Please choose a different one.')
        
    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user:
    #         raise ValidationError('That email is taken. Please choose a different one.')
    
class LoginForm(FlaskForm):

    email = StringField('Email address', validators=[
        InputRequired("Email is required"),
        Email(message='Invalid email address format')
    ])
    password = PasswordField('Password', validators=[
        InputRequired('Password is required'),
        Length(min=6, message='Password must be at least 6 characters')
    ])

    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
# to send email or make enquiry
class sendMessageAdmin(FlaskForm):
    email = StringField('Recipient', validators=[
    InputRequired("Email is required"),
    Email(message='Invalid email address format')
])
    message = TextAreaField('Message', render_kw={"rows": 15, "cols": 11}, validators=[ InputRequired("A message is required")])
    
    subject = StringField('Subject', validators=[
    InputRequired("A message is required")])
    
    submit = SubmitField('Send')
    
  #to update the user account  
class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired("Username is required"),
        Length(min=2, max=20, message='Username must be between 2 and 20 characters')
    ])
    email = StringField('Email address', validators=[
        InputRequired("Email is required"),
        Email(message='Invalid email address format')
    ])
    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update') 
    
    
    
    def validate_guest_email( email_address):
        try:
            valid = validate_email(email_address)
            return True
        except EmailNotValidError as e:
            return False
        
    # def validate_username(self, username):
    #     if username.data != current_user.username: 
    #         user = User.query.filter_by(username=username.data).first()
    #         if user:
    #          raise ValidationError('That username is taken. Please choose a different one.')
        
    # def validate_email(self, email):
    #     if email.data != current_user.email:
    #         user = User.query.filter_by(email=email.data).first()
    #         if user:
    #             raise ValidationError('That email is taken. Please choose a different one.')

