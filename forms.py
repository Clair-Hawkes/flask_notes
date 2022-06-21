"""Forms for notes app."""

from email.message import EmailMessage
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField, PasswordField
from wtforms.validators import InputRequired, Length, URL, Optional

class RegisterUserForm (FlaskForm):
    """Form for registering a User instance"""

    username = StringField(
        'Username: ',
        validators=[InputRequired(),Length(max=20)])

    password = PasswordField(
        'Password: ',
        # TODO: Length opf password in form affects Hash?
        validators=[InputRequired(),Length(max=100)]
    )

    # EmailField()
    email = StringField(
        'Email: ',
        validators=[InputRequired()])

    first_name = StringField(
        'First Name: ',
        validators=[InputRequired(),Length(max=30)])

    last_name = StringField(
        'Last Name: ',
        validators=[InputRequired(),Length(max=30)])








# email, first_name, and last_name.





#    name = StringField(
#         "Pet Name",
#         validators=[InputRequired()],
#     )

#     species = SelectField(
#         "Species",
#         choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
#     )