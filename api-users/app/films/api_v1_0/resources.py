from flask import request, Blueprint
from flask_restful import Api, Resource
from app.db import allCountries, oneCountry, addCountry

users_v1_0_bp = Blueprint('users_v1_0_bp', __name__)


api = Api(users_v1_0_bp)

class ExampleResource(Resource):
    def get(self):
        return 'This is an example'


class GetCountries(Resource):
    def get(self):
        return allCountries()

class OneCountry(Resource):
    def get(self):
        data = request.get_json()
        result = (oneCountry(data['value']))
        return result

    def post(self):
        data = request.get_json()
        result = (addCountry(data['value']))
        return(result)

api.add_resource(ExampleResource, '/api/v1.0/example')
api.add_resource(GetCountries, '/api/v1.0/getCountries')
api.add_resource(OneCountry, '/api/v1.0/onecountry')
