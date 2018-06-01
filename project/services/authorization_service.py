# -*- coding: utf-8 -*-

from base_service import BaseService

from project.business.authorization_business import AuthorizationBusiness

class AuthorizationService(BaseService):

    def do_signup(self, userData):
        try:
            authBus = AuthorizationBusiness()
            result = authBus.signup(userData)
            return self.return_success("user registred", {})
        except Exception as ex:
            return self.return_exception(ex)

    def do_login(self, authorization):
        try:
            authBus = AuthorizationBusiness()
            result = authBus.do_login(authorization)
            return self.return_success("user logged.", result)
        except Exception as ex:
            return self.return_exception(ex)
