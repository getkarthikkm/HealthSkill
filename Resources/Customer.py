from flask import request
from flask_restful import Resource

from helpers import create_item, read_items


class CustomerResource(Resource):

    def get(self):
        """
        Handler method for get operation.
        :return: tuple
        """
        args = request.args.to_dict()
        response = read_items(args)
        return response

    def post(self):
        """
        Handler method for post operation.
        :return: tuple
        """
        json_data = request.get_json(force=True)
        response = create_item(json_data)
        return response


