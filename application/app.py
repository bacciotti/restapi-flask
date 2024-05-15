from flask import jsonify
from flask_restful import Resource, reqparse
from mongoengine.errors import NotUniqueError
from .model import UserModel


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
        return {"message": "Users / get"}, 200


class User(Resource):
    def post(self):
        return {"message": "User / post"}, 200

    def get(self, cpf):
        return {"message": "User / get"}, 200
