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

    meta = {'allow_inheritance': True}


class UserModel(UserBase):
    """
    Common User
    """
    belonging_libraries = ListField(ReferenceField(LibraryModel, required=True))
    # 사용자가 속한 도서관들


class AdminModel(UserBase):
    """
    Admin
    """
    managing_library = ReferenceField(LibraryModel, required=True)
    # 관리하고 있는 도서관


class RefreshTokenModel(Document):
    """
    Manages Refresh Token
    """
    refresh_token = UUIDField(primary_key=True)
    owner = ReferenceField(UserBase, required=True)
    pw_snapshot = StringField(required=True)
