from ..config.database import db
from datetime import datetime, timedelta

class PasswordResetToken(db.Model):
    __tablename__ = "password_reset_token"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(64), nullable=False, unique=True)
    expiration = db.Column(db.DateTime, default=datetime.utcnow() + timedelta(hours=1))

    def __init__(self, user_id, token, expiration):
        self.user_id = user_id
        self.token = token
        self.expiration = expiration
  
    def get_all(cls):
        tokens = cls.query.all()
        return tokens
  

    def find_by_id(cls, id):
        token = cls.query.filter_by(id=id)
        return token

    def data(self):
        return {
        "user_id": self.user_id,
        "token": self.token,
        "expiration": self.expiration,
        }