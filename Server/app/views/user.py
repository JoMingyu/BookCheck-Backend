from uuid import uuid4

from flask import Response
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required
from flask_restful import Resource, request
from flasgger import swag_from


from app.models.user import UserModel, AdminModel, RefreshTokenModel


class Signup(Resource):
    def post(self):
        """
        일반 사용자 회원가입
        """
        id: str = request.form['id']
        pw: str = request.form['pw']

        if UserModel.objects(id=id):
            return Response('', 204)

        UserModel(id=id, pw=pw).save()

        return Response('', 201)

