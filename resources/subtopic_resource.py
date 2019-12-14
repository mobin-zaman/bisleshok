from flask_restful import Resource
from flask import request
from schemas.schema import SubTopicSchema
from models.subtopic import SubTopic
from analytics_backend.analytics import get_columns
from db import db


class SubTopicIdReport(Resource):

    def get(self, id):
        """url: /api/subtopic/<int:id>/<string:column_name>/report/"""
        """url: /api/subtopic/report/"""

        subtopic = SubTopic.query.get_or_404(id)

        column_names = subtopic.request_string1 + " , " + subtopic.request_string2

        sql = "select months, bank_categories, " + column_names + " from iig"
        print(sql)

        result = db.engine.execute(sql)

        rows = [row for row in result]

        result_dict = {
            "column": ['Month', 'Bank Category', 'Number Of Transactions', 'Amount Of Taka In Crore' ],
            "fields": [list(x) for x in rows ]
        }

        return result_dict
# result = get_columns(df, '2015-04-30', '2015-05-30', 'categories', 'agent_banking_no_of_agents', 'cheque_clearing_non_micr_amount_tk_in_crore')
