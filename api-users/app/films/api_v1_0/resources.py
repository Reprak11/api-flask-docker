from flask import request, Blueprint
from flask_restful import Api, Resource
from app.db import allCountries

users_v1_0_bp = Blueprint('users_v1_0_bp', __name__)


api = Api(users_v1_0_bp)

class ExampleResource(Resource):
    def get(self):
        return 'This is an example'

class ExampleResource2(Resource):
    def get(self):
        return 'This is an example 2'

class GetCountries(Resource):
    def get(self):
        return allCountries()


api.add_resource(ExampleResource, '/api/v1.0/example')
api.add_resource(ExampleResource2, '/api/v1.0/example2')
api.add_resource(GetCountries, '/api/v1.0/getCountries')
