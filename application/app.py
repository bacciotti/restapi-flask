from flask import jsonify
from flask_restful import Resource, reqparse


_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    "first_name", type=str, required=True, help="This field cannot be blank."
)
_user_parser.add_argument(
    "last_name", type=str, required=True, help="This field cannot be blank."
)
_user_parser.add_argument(
    "cpf", type=str, required=True, help="This field cannot be blank."
)
_user_parser.add_argument(
    "email", type=str, required=True, help="This field cannot be blank."
)
_user_parser.add_argument(
    "birth_date", type=str, required=True, help="This field cannot be blank."
)


class Users(Resource):
    def get(self):
        return {"message": "Users / GET"}, 200


class User(Resource):
    def post(self):
        return {"message": "User / POST"}, 200

    def patch(self):
        return {"message": "User / PATCH"}, 200

    def delete(self):
        return {"message": "User / DELETE"}, 200

    def get(self, cpf):
        return {"message": "User / GET"}, 200


class HealthCheck(Resource):
    def get(self):
        return jsonify({"status": "UP"}), 200
