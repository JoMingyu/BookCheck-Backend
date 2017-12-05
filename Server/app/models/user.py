from datetime import datetime

from app.models import *
from app.models.library import LibraryModel


class UserBase(Document):
    """
    User Base Collection
    """
    signup_time = DateTimeField(required=True, default=datetime.now())

    id = StringField(primary_key=True)
    pw = StringField(required=True)
    belonging_libraries = ListField(ReferenceField(LibraryModel, required=True))
    # 사용자가 속한 도서관

    meta = {'allow_inheritance': True}


# 의도적으로 Collection을 나누기 위한 상속 구조
class UserModel(UserBase):
    """
    Common User
    """
    pass


class AdminModel(UserBase):
    """
    Admin
    """
    pass


class RefreshTokenModel(Document):
    """
    Manages Refresh Token
    """
    refresh_token = UUIDField(primary_key=True)
    owner = ReferenceField(UserBase, required=True)
    pw_snapshot = StringField(required=True)
