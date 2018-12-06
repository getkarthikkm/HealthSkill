from flask import Blueprint
from flask_restful import Api
from Resources.Customer import CustomerResource

api_bp = Blueprint('skill', __name__)
api = Api(api_bp)

# Route
api.add_resource(CustomerResource, '/health')
