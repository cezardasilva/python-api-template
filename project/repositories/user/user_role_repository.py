# -*- coding: utf-8 -*-

#from peewee import *
from project.repositories.base_respository import *

class UserRoleRepository(Document):

    #id = AutoField()
    role = StringField()

    #class Meta:
    #    table_name = 'user_role'
