# -*- coding: utf-8 -*-

import datetime
import hashlib
#from peewee import *
from werkzeug.security import generate_password_hash, check_password_hash
from project.repositories.base_respository import *
from project.repositories.user.user_role_repository import UserRoleRepository

class UserRepository(Document):

    username = EmailField(max_length=180, unique=True)
    public_id = StringField(max_length=126, unique=True)
    password = StringField(max_length=128)
    trading_name = StringField(max_length=180)
    document_id = StringField(max_length=20)
    user_role = ReferenceField(UserRoleRepository)
    created_at = DateTimeField(default=datetime.datetime.utcnow)

    def check_email_exists(self, _username):
        result = UserRepository.objects(username=_username)[:1]
        return result[0] if len(result) > 0 else None

    def get_by_publicid(self, public_id):
        result = UserRepository.objects(public_id=public_id)[:1]
        return result[0] if len(result) > 0 else None

    @staticmethod
    def hash_password(password):
        hashed = generate_password_hash(password.encode('utf8'), method="sha1")
        return hashed

    @staticmethod
    def check_password(password_from_user, password_from_auth):
        return check_password_hash(password_from_user, password_from_auth)
