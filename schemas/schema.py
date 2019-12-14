from models.index import Index
from models.topic import Topic
from models.subtopic import SubTopic
from marshmallow_sqlalchemy import ModelSchema

class IndexSchema(ModelSchema):
    class Meta:
        model = Index

class TopicSchema(ModelSchema):
    class Meta:
        model = Topic
        exclude = ['subtopics']

class SubTopicSchema(ModelSchema):
    class Meta:
        model = SubTopic
