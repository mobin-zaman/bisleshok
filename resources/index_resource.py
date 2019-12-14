from flask_restful import Resource
from schemas.schema import *

from models.index import Index
from models.topic import Topic



class IndexResource(Resource):
    def get(self): 
        """it is going to send the information of a particular index
        if id is provided, else it will return all the indexes"""
        """potential url : /api/index/"""
        """TODO: need to find out what does the endpoint attribute do in the api objects"""
        all_index=Index.query.all()

        result = IndexSchema(many=True).dump(all_index)

        print(result)

        return result,200

class IndexIdResource(Resource):
    """/api/index/<int:id>"""
    def get(self,id):

        index = Index.query.get_or_404(id)

        result = IndexSchema().dump(index)

        print(result)

        return result,200
        
class IndexIdTopic(Resource):
    """/api/index/<int:id>/index"""
    def get(self,id):
        index = Index.query.get_or_404(id)
        topic = Topic.query.filter_by(index_id=index.id).all()

        topic = TopicSchema(many=True).dump(topic)

        return topic,200



        


