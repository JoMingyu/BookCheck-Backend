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


class AuthCommonUser(Resource):
    def post(self):
        """
        일반 사용자 로그인
        """
        id: str = request.form['id']
        pw: str = request.form.get['pw']

        user = UserModel.objects(id=id, pw=pw).first()

        if not user:
            return Response('', 401)

        refresh_token = uuid4()
        RefreshTokenModel(refresh_token=refresh_token, owner=user, pw_snapshot=pw).save()

        return {
            'access_token': create_access_token(id),
            'refresh_token': create_refresh_token(str(refresh_token))
        }, 200


class AuthAdmin(Resource):
    def post(self):
        """
        관리자 로그인
        """
        id: str = request.form['id']
        pw: str = request.form.get['pw']

        admin = AdminModel.objects(id=id, pw=pw).first()

        if not admin:
            return Response('', 401)

        refresh_token = uuid4()
        RefreshTokenModel(refresh_token=refresh_token, owner=admin, pw_snapshot=pw).save()

        return {
            'access_token': create_access_token(id),
            'refresh_token': create_refresh_token(str(refresh_token))
        }, 200


class Refresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        """
        새로운 Access Token 발급
        """
        refresh_token = RefreshTokenModel.objects(refresh_token=get_jwt_identity())

        if not refresh_token:
            return Response('', 403)

        if refresh_token.owner.pw != refresh_token.pw_snapshot:
            return Response('', 205)

        return {
            'access_token': create_access_token(refresh_token.owner.id)
        }, 200
