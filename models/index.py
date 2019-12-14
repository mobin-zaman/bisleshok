from db import db

class Index(db.Model):
    """the entity for the start page"""
    """need to add added_on and edited_on"""
    id=db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(300),nullable=False,unique=True)
    topics= db.relationship('Topic',backref='index', lazy='dynamic') #what does lazy = 'dynamic' do?
    roman_index=db.Column(db.String(100))




