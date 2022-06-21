"""Flask app for Notes"""

from flask import Flask, request, jsonify, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import RegisterUserForm
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['SQLALCHEMY_ECHO'] = True

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.get('/')
def root():
    """Redirect user to register page"""

    return redirect('/register')

@app.route('/register', methods=['GET','POST'])
def user_register():
    """
        GET: Show a form that when submitted will register/create a user.
        POST: Handle form submission and register user in db.
    """

    # form = EditPetForm(obj=pet)
    form = RegisterUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User.register(
            username = username,
            password = password,
            email = email,
            first_name = first_name,
            last_name = last_name
        )
        db.session.add(user)
        db.session.commit()

        session["username"] = user.username


        return redirect('/secret')

    else:
        return render_template('register.html',form=form)


