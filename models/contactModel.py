from datetime import datetime
from middlewares.dbconfig import db

class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(255), nullable=True)
    message = db.Column(db.Text, nullable=False)
    contactDate = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Contact {self.name}>"
