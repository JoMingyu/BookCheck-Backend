import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.library.library import *
from app.models.library import LibraryModel
from app.models.user import UserModel


class Library(Resource):
    @swag_from(LIBRARY_POST)
    @jwt_required
    def post(self):
        """
        도서관에 가입
        """
        user = UserModel.objects(id=get_jwt_identity()).first()

        if not user:
            return Response('', 403)

        library_id = request.form['library_id']
        library = LibraryModel.objects(id=library_id).first()
        if not library:
            # 존재하지 않는 Library ID
            return Response('', 204)

        if library in user.belonging_libraries:
            # 이미 가입되어 있음
            return Response('', 208)

        user.belonging_libraries.append(library)
        user.save()

        return Response('', 201)

    @swag_from(LIBRARY_GET)
    @jwt_required
    def get(self):
        """
        도서관 리스트 조회
        """
        user = UserModel.objects(id=get_jwt_identity()).first()

        if not user:
            return Response('', 403)

        return Response(json.dumps(
            [{
                'id': str(library.id),
                'title': library.title,
                'belonging': library in user.belonging_libraries
            } for library in LibraryModel.objects], ensure_ascii=False
        ), 200, content_type='application/json; charset=utf8')

    @swag_from(LIBRARY_DELETE)
    @jwt_required
    def delete(self):
        """
        도서관에서 탈퇴
        """
        user = UserModel.objects(id=get_jwt_identity()).first()

        if not user:
            return Response('', 403)

        library_id = request.form['library_id']
        library = LibraryModel.objects(id=library_id).first()
        if not library:
            # 존재하지 않는 Library ID
            return Response('', 204)

        if library not in user.belonging_libraries:
            # 애초에 가입되어 있지 않음
            return Response('', 208)

        user.belonging_libraries.remove(library)
        user.save()

        return Response('', 200)
