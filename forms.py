"""Forms for notes app."""

from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import InputRequired, Length, Email
import email_validator

class RegisterUserForm (FlaskForm):
    """Form for registering a User instance"""

    username = StringField(
        'Username',
        validators=[InputRequired(),Length(max=20)])

    password = PasswordField(
        'Password',
        validators=[InputRequired(),Length(max=100)]
    )

    # EmailField()
    email = StringField(
        'Email',
        validators=[InputRequired(),Email()])

    first_name = StringField(
        'First Name',
        validators=[InputRequired(),Length(max=30)])

    last_name = StringField(
        'Last Name',
        validators=[InputRequired(),Length(max=30)])


class LoginUserForm(FlaskForm):
    """Form will log in a user"""

    username = StringField(
        'Username',
        validators=[InputRequired(),Length(max=20)])

    password = PasswordField(
        'Password',
        validators=[InputRequired(),Length(max=100)])


class LogoutUserForm(FlaskForm):
    """
    Form will log out a user
    Just for CSRF Protection
    """

