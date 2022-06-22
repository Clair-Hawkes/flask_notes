"""Models for Notes app."""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model):
    """
    Creates a user instance.
    Class Methods:
    check_if_details_avail - Checks for unique username/ email.
    register - Registers a user to database with hashed password.
    authenticate - Validates User authentication.
    """

    __tablename__ = "users"

    username = db.Column(
        db.String(20),
        primary_key=True)
    password = db.Column(
        db.String(100),
        nullable=False)
    email = db.Column(
        db.String(50),
        nullable=False,
        unique=True)
    first_name = db.Column(
        db.String(30),
        nullable=False)
    last_name = db.Column(
        db.Text,
        nullable=False)

    @classmethod
    def check_if_details_avail(cls, username, email):
        """
        Check if username or email has been taken by another user.
        u - username, e -email
        returns True/False
        """

        u = cls.query.filter_by(username=username).one_or_none()
        e = cls.query.filter_by(email=email).one_or_none()

        if u or e:
            return False

        return True

    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """
        Register user w/hashed password & return user.
        Returns a new user instance
        """

        hashed = bcrypt.generate_password_hash(password).decode('utf8')

        # return instance of user w/username and hashed pwd
        return cls(
            username=username,
            password=hashed,
            email=email,
            first_name=first_name,
            last_name=last_name)

    @classmethod
    def authenticate(cls, username, password):
        """
        Validate that a user exists and that the password matches stored
        hashed value in database.
        Accepts username,password.
        Returns User Instance
        """

        user = cls.query.filter_by(username=username).one_or_none()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False


class Note(db.Model):
    """
    Creates a note instance.
    """

    __tablename__ = "notes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)
    title = db.Column(
        db.String(100),
        nullable=False)
    content = db.Column(
        db.Text,
        nullable=False)
    owner = db.Column(
        db.String(20),
        db.ForeignKey('users.username'))

    users = db.relationship('User', backref='notes')

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
