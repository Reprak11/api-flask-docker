from flask import request, Blueprint
from flask_restful import Api, Resource
from app.dbCountries import allCountries, oneCountry, addCountry
from app.dbUsers import addUser, allUsers
from app.createTables import createTables

users_v1_0_bp = Blueprint('users_v1_0_bp', __name__)

api = Api(users_v1_0_bp)

class ExampleResource(Resource):
    def get(self):
        return 'This is an example'

#Countries Table Resources
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

#Users Table Resources
class OneUser(Resource):
    def get(self):
        return "Hola Get"
    def post(self):
        data = request.get_json()
        if ("first_name" in data and "last_name" in data and "birthday" in data and "country" in data):
            return addUser(data)
        else:
            return "Missing Values"

class GetUsers(Resource):
    def get(self):
        return(allUsers())

class CreateMyTables(Resource):
    def post(self):
        return(createTables())

api.add_resource(ExampleResource, '/api/v1/0/example')
api.add_resource(GetCountries, '/api/v1/0/getcountries')
api.add_resource(OneCountry, '/api/v1/0/onecountry')
api.add_resource(GetUsers, '/api/v1/0/getusers')
api.add_resource(OneUser, '/api/v1/0/oneuser')
api.add_resource(CreateMyTables, '/api/v1/0/createtable')
