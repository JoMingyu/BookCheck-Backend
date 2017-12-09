from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.library.borrow import *
from app.models.library import BookModel, BorrowModel
from app.models.user import UserModel, AdminModel


class Borrow(Resource):
    @swag_from(BORROW_POST)
    @jwt_required
    def post(self):
        """
        책 반납
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()

        if not admin:
            return Response('', 403)

        rfid = request.form['rfid']
        book = BookModel.objects(rfid=rfid).first()

        if not book:
            # 존재하지 않는 RFID
            return Response('', 204)

        if admin.managing_library != book.belonging_library:
            # 자기 관할의 도서관이 아님
            return Response('', 403)

        if book.borrowable:
            # 이미 반납되어 책이 대출 가능한 상태
            return Response('', 208)

        BorrowModel.objects(book=book).delete()
        book.update(borrowable=True)

        return Response('', 200)

    @swag_from(BORROW_GET)
    @jwt_required
    def get(self):
        """
        도서관에서 책 대출
        """
        user = UserModel.objects(id=get_jwt_identity()).first()

        if not user:
            return Response('', 403)

        rfid = request.args['rfid']
        book = BookModel.objects(rfid=rfid).first()

        if not book:
            # 존재하지 않는 RFID
            return Response('', 204)

        if not book.borrowable:
            # 대출 불가능한 책
            return Response('', 208)

        if book.belonging_library not in user.belonging_libraries:
            # 가입되어 있지 않은 도서관
            return Response('', 403)

        BorrowModel(book=book, borrower=user.id).save()
        book.update(borrowable=False)

        return Response('', 200)
