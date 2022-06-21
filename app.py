"""Flask app for Notes"""

from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import RegisterUserForm, LoginUserForm, LogoutUserForm
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


@app.route('/register', methods=['GET', 'POST'])
def user_register():
    """
        GET: Show a form that when submitted will register/create a user.
        POST: Handle form submission and register user in db if valid input and
        redirects to user page.
    """

    form = RegisterUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        if User.check_if_details_avail(username=username, email=email):
            user = User.register(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            db.session.add(user)
            db.session.commit()

            session["username"] = user.username
            return redirect(f"/users/{session['username']}")

        else:
            form.username.errors = ["Bad username/email"]

    return render_template('register.html', form=form)


@app.get('/secret')
def secret():
    """Displays secret html page only accessible by direct get request.
    If user not logged in redirects to /login."""

    if 'username' in session:
        return "You made it!"
    else:
        return redirect('/login')


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    GET: Show a form that when submitted will login a user.
    POST: Process login form and pass username to session.
    """

    form = LoginUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            session["username"] = user.username
            return redirect(f"/users/{session['username']}")

        else:
            form.username.errors = ["Bad name/password"]

    return render_template("login.html", form=form)


@app.get('/users/<username>')
def user_info(username):
    """
    Displays a template showing information about the user.
    (everything except for their password)
    """

    if session['username'] != username:
        return redirect('/login')

    user = User.query.get_or_404(username)

    form = LogoutUserForm()

    return render_template('user_page.html', form=form, user=user)


@app.post('/logout')
def user_logout():
    """Clear username from session and redirect to root route/"""

    form = LogoutUserForm()

    if form.validate_on_submit():
        session.pop('username', None)

    return redirect('/')
