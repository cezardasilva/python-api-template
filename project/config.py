# -*- coding: utf-8 -*-
import os

class Server():

    BASE_PATH='/'
    API_VERSION='v1'
    SECRET_KEY='PUTASECRETTOKENHERE'
    TMP_DIR = 'project/tmp/'

    NOSQL_HOST=os.environ['NOSQL_HOST']

    SERVER_DEBUG=os.environ['SERVER_DEBUG']
    SERVER_URL=os.environ['SERVER_URL']

    def get_base_path(self):
        return self.BASE_PATH + self.API_VERSION

    @staticmethod
    def get_secret_key():
        return self.SECRET_KEY


class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
