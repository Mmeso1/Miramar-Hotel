from ..config.database import db

class Room(db.Model):
    __tablename__ = "room"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room_name = db.Column(db.String(80), nullable=False, unique=True)
    image1 = db.Column(db.String(255))
    image2 = db.Column(db.String(255))
    image3 = db.Column(db.String(255))
    view = db.Column(db.String(80))
    width = db.Column(db.String(80))
    max_occupancy = db.Column(db.Integer)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default="available")

    
    def __init__(self, room_name, image1, image2, image3, view, width, max_occupancy, price, description, status="available"):
        self.room_name = room_name
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.view = view
        self.width = width
        self.max_occupancy = max_occupancy
        self.price = price
        self.description = description
        self.status = status

    
  
    def get_all(cls):
        rooms = cls.query.all()
        return rooms
  

    def find_by_id(cls, id):
        room = cls.query.filter_by(id=id)
        return room

    def data(self):
        return {
        "room_name": self.room_name,    
        "image1": self.image1,
        "image2": self.image2,
        "image3": self.image3,
        "view": self.view,
        "width": self.width,
        "max_occupancy": self.max_occupancy,
        "price": self.price,
        "description": self.description,
        "status": self.status,
        }