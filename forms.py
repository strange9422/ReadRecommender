from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField ,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
#from wtforms.validators import*

#from main1 import User



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                              validators=[DataRequired(),Length(min=2,max=20)])

    email = StringField('Email',
                              validators=[DataRequired(),Email()])

    age=IntegerField('Age',
                           validators=[DataRequired()])

    password =PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm_Password',
                                               validators=[DataRequired(),EqualTo('password')])

    submit=SubmitField('Sign Up')

    # def validate_username(self,username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if True:
    #         raise ValidationError('That username is taken . Please choose different one.')
    #
    # def validate_email(self,email):
    #     user = User.query.filter_by(username=email.data).first()
    #     if True:
    #         raise ValidationError('That email is taken . Please choose different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    remember= BooleanField('Remember Me')
    submit = SubmitField('Login')

class Post_form(FlaskForm):
    book_name =StringField('Book',validators=[DataRequired()])
    rating = IntegerField('Rating',
                       validators=[DataRequired()])
    userid = IntegerField('User_id',
                          validators=[DataRequired()])

    submit = SubmitField('Submit')
