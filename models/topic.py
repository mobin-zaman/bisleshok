from db import db

class Topic(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(250),nullable=False, unique=True)
    index_id=db.Column(db.Integer, db.ForeignKey('index.id'))
    subtopics=db.relationship('SubTopic',backref='subtopic',lazy='dynamic')
    
