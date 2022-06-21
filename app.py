"""Flask app for Notes"""

from flask import Flask, request, jsonify, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
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


