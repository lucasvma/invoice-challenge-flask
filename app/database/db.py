from flask_sqlalchemy import SQLAlchemy
import os
from server import application

basedir = os.path.abspath(os.path.dirname(__file__))
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
session = SQLAlchemy(application)
