from datetime import datetime, timedelta

from app.models import *

from app.models.user import UserModel


class LibraryModel(Document):
    """
    도서관
    """
    id = StringField(primary_key=True)
    # ObjectID는 사용자가 입력하기 너무 김
    title = StringField(required=True)


class BookModel(Document):
    """
    책
    """
    rfid = StringField(primary_key=True)
    belonging_library = ReferenceField(LibraryModel, required=True)
    area = IntField(required=True)
    # 책의 RFID와 속해 있는 도서관, area

    title = StringField(required=True)
    author = StringField(required=True)
    publication_date = DateTimeField(required=True)
    summary = StringField(required=True)
    detail = StringField(required=True)
    # 책에 대한 기본 정보

    borrowable = BooleanField(required=True, default=True)
    # 대출 가능 여부


class BorrowModel(Document):
    """
    대출
    """
    book = ReferenceField(BookModel, required=True)
    borrower = ReferenceField(UserModel, required=True)
    borrow_limit = DateTimeField(required=True, default=datetime.now().date() + timedelta(days=7))
    # 반납 기한(기본값은 7일 이후)


class LightModel(Document):
    """
     점등 데이터 관리
     구현 보류
    """
    library = ReferenceField(LibraryModel, required=True)
    book = ReferenceField(BookModel, required=True)
    # 점등이 필요한 책
    light_color = StringField()
    # None일 수 있음(None은 소등해야 함을 의미)
