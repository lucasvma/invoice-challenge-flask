from flask import Flask
import app.controllers.users
import app.models.users

application = Flask(__name__)
