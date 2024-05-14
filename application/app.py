from flask import jsonify
from flask_restful import Resource, reqparse
from mongoengine.errors import NotUniqueError
from .models import UserModel


_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank.")
_user_parser.add_argument('last_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank.")
_user_parser.add_argument('cpf',
                          type=str,
                          required=True,
                          help="This field cannot be blank.")
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help="This field cannot be blank.")
_user_parser.add_argument('birth_date',
                          type=str,
                          required=True,
                          help="This field cannot be blank.")


class Users(Resource):
    def get(self):
        return jsonify(UserModel.objects())


class User(Resource):
    def post(self):
        data = _user_parser.parse_args()

        try:
            response = UserModel(**data).save()
            return {
                'message': 'User %s created successfully' % response.first_name
            }
        except NotUniqueError:
            return {
                'message': 'CPF already exists in the database.'
            }

    def get(self, cpf):
        response = UserModel.objects(cpf=cpf)

        if response:
            return jsonify(response)

        return {"message": "User not found."}, 400
