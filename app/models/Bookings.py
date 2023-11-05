from ..config.database import db

class Booking(db.Model):
    __tablename__ = "booking"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_of_arrival = db.Column(db.Date, nullable=False)
    date_of_departure = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default="pending")
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room = db.relationship('Room', backref='bookings', lazy=True)

    def __init__(self, date_of_arrival, date_of_departure, status, room_id, user_id):
        self.date_of_arrival = date_of_arrival
        self.date_of_departure = date_of_departure
        self.status = status
        self.room_id = room_id
        self.user_id = user_id

    
  
    def get_all(cls):
        bookings = cls.query.all()
        return bookings
  

    def find_by_id(cls, id):
        booking = cls.query.filter_by(id=id)
        return booking

    def data(self):
        return {
        "date_of_arrival": self.date_of_arrival,
        "date_of_departure": self.date_of_departure,
        "status": self.status,
        "room_id": self.room_id,
        "user_id": self.user_id,
        }
    