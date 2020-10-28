from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,EqualTo, Email


#DataRequired == Making sure the field in
#Equalto == Naking sure the field(s)  are the same (ie. Password and Confirm Password)
#Email == Making sure the field has a proper email given

class UserInfoForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Username', validators = [DataRequired()])
    confirm_pass = PasswordField('Username', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()
