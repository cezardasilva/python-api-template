# -*- coding: utf-8 -*-
import sys
import logging
import traceback
from array import *
from flask import make_response, jsonify
from slackclient import SlackClient

from project.config import Server
from project.framework.exception.exceptions import *
from project.business.authorization_business import AuthorizationBusiness

class BaseService():
	logged_user = None

	def __init__(self, accessData=None):
		logging.basicConfig(filename='api.log',level=logging.DEBUG)

		if accessData:
			self.set_logged_user(accessData)

	def set_logged_user(self, authData):
		authBuss = AuthorizationBusiness()
		logged_user = authBuss.get_logged_user(authData)
		self.logged_user = logged_user

	def admin_method(self):
		if not self.logged_user.user_role.name == 'admin':
			raise NotAuthorizedException("Only to admin!")

	def return_success(self, message, details):
		if message is None:
			message = 'Ok'
		return make_response(jsonify({'code': 200, 'message': message, 'details': details}), 200)

	def return_exception(self, ex):
		http_code = 400
		if isinstance(ex, BusinessException):
			exception = {
				'exceptions': [{
					'type': ex.type,
					'message': ex.message,
				}]
			}
		elif isinstance(ex, NotAuthorizedException):
			http_code = 401
			exception = {
						'exceptions': [
							{
								'type': ex.type,
								'message': ex.message
							}
						]
					}
		else:
			http_code = 500
			exception = {
				'exceptions': [{
					'message': [str(x) for x in ex.args],
				}]
			}
		logging.debug(traceback.format_exc())
		return make_response(jsonify({'code': http_code, 'exceptions': exception, 'traceback': traceback.format_exc()}), http_code)
