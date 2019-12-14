from flask_restful import Resource
from schemas.schema import TopicSchema, SubTopicSchema
from models.topic import Topic
from models.subtopic import SubTopic
class TopicIdResource(Resource):
    """potential url: /api/topic/<int:id>"""
    def get(self,id):

        topic = Topic.query.get_or_404(id)
        result = TopicSchema().dump(topic)
        print(result)

        return result,200
#FIXME: another end point might be needed in order to get topic id
#from index id, but index already provides the topic ids

class TopicIdSubTopic(Resource):
    """potential url: /api/topic/<int:id>/subtopic"""

    def get(self,id):


        subtopic = SubTopic.query.filter_by(topic_id=id).all()

        result = SubTopicSchema(many=True).dump(subtopic)

        return result,200


        pass









