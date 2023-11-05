from ..config.database import db
from datetime import datetime
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), default="user")
    image = db.Column(db.String, nullable=True, default="https://images.pexels.com/photos/1751279/pexels-photo-1751279.jpeg?auto=compress&cs=tinysrgb")
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    bookings = db.relationship('Booking', backref='user', lazy=True, foreign_keys="Booking.user_id")

    def __init__(self, username, email, password, role="user", image=None, date_created=None):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role
        self.image = image
        if date_created is None:
            date_created = datetime.utcnow()
        self.date_created = date_created
  
    def get_all(cls):
        users = cls.query.all()
        return users
  

    def find_by_id(cls, id):
        user = cls.query.filter_by(id=id).first()
        return user

    def data(self):
        return {
        "username": self.username,
        "email": self.email,
        "role": self.role,
        "image": self.image,
        "date_created": self.date_created,
        }