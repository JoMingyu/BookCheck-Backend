import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.models.library import LibraryModel, BookModel
from app.models.user import UserModel, AdminModel
from app.support.mongo_helper import mongo_to_dict


class Book(Resource):
    @jwt_required
    def post(self):
        """
        도서관에 책 추가
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()

        if not admin:
            return Response('', 403)

        library_id: str = request.form['library_id']
        library = LibraryModel.objects(id=library_id)
        if not library:
            # 존재하지 않는 Library ID
            return Response('', 204)

        rfid: str = request.form['rfid']
        if BookModel.objects(rfid=rfid):
            # 이미 존재하는 RFID
            return Response('', 208)

        area: int = int(request.form['area'])
        title: str = request.form['title']
        author: str = request.form['author']
        publication_date: str = request.form['publication_date']
        summary: str = request.form['summary']
        detail: str = request.form['detail']

        BookModel(
            rfid=rfid,
            belonging_library=library,
            area=area,
            title=title,
            author=author,
            publication_date=publication_date,
            summary=summary,
            detail=detail
        ).save()

        return Response('', 201)

    @jwt_required
    def get(self):
        """
        도서관의 책 목록 조회
        """
        library_id: str = request.form['library_id']
        user = UserModel.objects(id=get_jwt_identity()).first()

        if not user or library_id not in user.belonging_libraries:
            return Response('', 403)

        library = LibraryModel.objects(id=library_id)
        if not library:
            # 존재하지 않는 Library ID
            return Response('', 204)

        return Response(json.dumps(
            [mongo_to_dict(book) for book in BookModel.objects(belonging_library=library)], ensure_ascii=False
        ), 200, content_type='application/json; charset=utf8')
