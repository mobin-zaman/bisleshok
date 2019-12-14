from db import db


class SubTopic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    request_string1 = db.Column(db.String(200), nullable=False)
    request_string2 = db.Column(db.String(200), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
