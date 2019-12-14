from flask import Flask

from flask_restful import Api

from flask_migrate import Migrate

from db import db

from resources.index_resource import IndexResource,IndexIdResource,IndexIdTopic
from resources.topic_resource import TopicIdResource, TopicIdSubTopic
from resources.subtopic_resource import SubTopicIdReport

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:@localhost/bisleshok"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

app.secret_key="jose"
api=Api(app)
migrate=Migrate(app,db)

api.add_resource(IndexResource,'/api/index/')
api.add_resource(IndexIdResource,'/api/index/<int:id>/')
api.add_resource(IndexIdTopic,'/api/index/<int:id>/topic/')
api.add_resource(TopicIdResource, '/api/topic/<int:id>/')
api.add_resource(TopicIdSubTopic,'/api/topic/<int:id>/subtopic/')
api.add_resource(SubTopicIdReport,'/api/subtopic/report/<int:id>/')

@app.route('/',methods=['GET'])
def test():
    return "working fine"

if __name__ == "__main__":
    db.init_app(app)
    app.run('0.0.0.0',port=3000,debug=True)

