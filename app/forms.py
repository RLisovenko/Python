from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("username",validators=[DataRequired()])
    password = PasswordField("PassWord",validators=[DataRequired()])
    remember_me = BooleanField("Save")
    submit = SubmitField("Enter")