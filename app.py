"""Flask app for Notes"""

from flask import Flask, request, jsonify, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import RegisterUser
from models import db, connect_db, User
# from forms import TODO:

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
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
    Show a form that when submitted will register/create a user.
    """

    # form = EditPetForm(obj=pet)
    form = RegisterUser()

    # if form.validate_on_submit():

    # else: TODO: Else return html + form standard

    return render_template('register.html',form=form)



