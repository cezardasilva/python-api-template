# -*- coding: utf-8 -*-

import datetime
from project.repositories.base_respository import *
from project.repositories.user.user_repository import UserRepository

class UserSessionRepository(Document):

    user = ReferenceField(UserRepository)
    created_at = DateTimeField(default=datetime.datetime.utcnow)

    #class Meta:
    #    table_name = 'user_session'
