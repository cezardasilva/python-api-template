# -*- coding: utf-8 -*-

#from peewee import *
import datetime
from project.config import Server
from mongoengine import *
#mysql_db = MySQLDatabase(Server().MYSQL_DATABASE, user=Server().MYSQL_USER, password=Server().MYSQL_PASSWORD, host=Server().MYSQL_HOST)

connect('dev', host=Server().NOSQL_HOST)

#class BaseRepository(Document):

    #class Meta:
    #    database = mysql_db

    #def prepare_update_params(self, params):
    #    for key, value in params.iteritems():
    #        setattr(self, key, value)

    #def save(self, *args, **kwargs):
    #    if self._pk is None:
    #        self.created_at = datetime.datetime.now()
    #    self.updated_at = datetime.datetime.now()
    #    return super(BaseRepository, self).save(*args, **kwargs)
