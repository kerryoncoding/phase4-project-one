from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData

db = SQLAlchemy(metadata=MetaData)

class Squad(db.Model):
   __tablename__ = 'Squads'

   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String)
   podcast = db.Column(db.String)

   def __repr__(self):
        return f'<Squad {self.id}, {self.name},{self.podcast}>'


class User(db.Model):
   __tablename__ = 'users'

   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True, nullable=False, index=True)
   email = db.Column(db.String(120), unique=True)
   verified = db.Column(db.Boolean, default=False)

   def __repr__(self):
        return f'<User {self.id}, {self.username}, {self.email}, {self.verified}>'