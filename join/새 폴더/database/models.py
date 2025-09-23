import flask_login
from database.session import db, login_manager
from config import JsonConfig

def get_model(model):
    if JsonConfig.get_data('TESTING'):
        return model.test_model
    return model

class UserMixin:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True)
    nickname = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(255))
    age = db.Column(db.Integer)

class TestUserModel(UserMixin, db.Model):
    __tablename__ = 'test_users'

class UserModel(UserMixin, flask_login.UserMixin, db.Model):
    __tablename__ = 'users'

    test_model = TestUserModel


User = get_model(UserModel)