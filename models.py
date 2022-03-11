from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager

login = LoginManager()
db_user = SQLAlchemy()

class UserModel(UserMixin, db_user.Model):
    __tablename__ = "users"

    id = db_user.Column(db_user.Integer, primary_key=True)
    email = db_user.Column(db_user.String(80), unique=True)
    username = db_user.Column(db_user.String(100))
    password_hash = db_user.Column(db_user.String())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return UserModel.query.get(int(id))