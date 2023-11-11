from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pets"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.String(20),
                     nullable=False)
    
    species = db.Column(db.String(20),
                        nullable=False)
    
    photo_url = db.Column(db.String(50))

    age = db.Column(db.Integer)

    notes = db.Column(db.String(200))

    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)

