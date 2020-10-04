from flask_marshmallow import Marshmallow

from app.database.db import session
from server import app

ma = Marshmallow(app)


class User(session.Model):
    id = session.Column(session.Integer, primary_key=True)
    username = session.Column(session.String(80), unique=True)
    email = session.Column(session.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
