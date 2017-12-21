import json

from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.library.book import *
from app.models.library import LibraryModel, BookModel
from app.models.user import UserModel, AdminModel
from app.support.mongo_helper import mongo_to_dict


class Book(Resource):
    @swag_from(BOOK_POST)
    @jwt_required
    def post(self):
        """
        도서관에 책 추가
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()

        if not admin:
            return Response('', 403)

        library_id = request.form['library_id']
        library = LibraryModel.objects(id=library_id).first()
        if not library:
            # 존재하지 않는 Library ID
            return Response('', 204)

        if admin.managing_library != library:
            # 자기 관할의 도서관이 아님
            return Response('', 403)

        rfid = request.form['rfid']
        if BookModel.objects(rfid=rfid):
            # 이미 존재하는 RFID
            return Response('', 208)

        area = int(request.form['area'])
        title = request.form['title']
        author = request.form['author']
        publication_date = request.form['publication_date']
        summary = request.form['summary']
        detail = request.form['detail']

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

    @swag_from(BOOK_GET)
    @jwt_required
    def get(self):
        """
        도서관의 책 목록 조회
        """
        library_id = request.args['library_id']
        user = UserModel.objects(id=get_jwt_identity()).first()

        if not user:
            return Response('', 403)

        library = LibraryModel.objects(id=library_id).first()
        if not library:
            # 존재하지 않는 Library ID
            return Response('', 204)

        if library not in user.belonging_libraries:
            # 가입되어 있지 않은 도서관
            return Response('', 403)

        keyword = request.args.get('keyword')

        if not keyword:
            return Response(json.dumps(
                [mongo_to_dict(book, ['belonging_library']) for book in BookModel.objects(belonging_library=library)], ensure_ascii=False
            ), 200, content_type='application/json; charset=utf8')
        else:
            return Response(json.dumps(
                [mongo_to_dict(book, ['belonging_library']) for book in BookModel.objects(belonging_library=library) if keyword in book.title], ensure_ascii=False
            ), 200, content_type='application/json; charset=utf8')
