from datetime import datetime
from middlewares.dbconfig import db

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(255), nullable=True)
    postDate = db.Column(db.String(50), nullable=False)
    popular = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Post {self.title}>"
