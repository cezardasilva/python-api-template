# -*- coding: utf-8 -*-
import uuid
import jwt
import hashlib
import datetime
from itsdangerous import TimestampSigner
from project.config import Server
from project.framework.exception.exceptions import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from project.repositories.user.user_repository import UserRepository
from project.repositories.user.user_role_repository import UserRoleRepository
from project.repositories.user.user_session_repository import UserSessionRepository

class AuthorizationBusiness():

    def signup(self, userData):
        self.validate_signup_data(userData)

        user = UserRepository().check_email_exists(userData['username'])
        if user == None:
            userData['password'] = UserRepository().hash_password(userData['password'])
            userData['public_id'] = str(uuid.uuid4())
            if 'retype_password' in userData:
                userData.pop('retype_password')
            new_user = UserRepository(**userData).save()
            user_role = UserRoleRepository.objects(role='user')[:1]
            new_user.user_role = user_role[0]
            new_user.save()
            return new_user
        else:
            raise BusinessException("User already registred.")

    def do_login(self, authorization):
        if not authorization or not authorization.username or not authorization.password:
            raise BusinessException("Authorization header not found")
        user = UserRepository().check_email_exists(authorization.username)
        if not user:
            raise BusinessException('User not found, check you username.')
        print user.password

        if not UserRepository().check_password(user.password, authorization.password):
            raise BusinessException('Wrong password.')
        login_token = self.get_login_token(user)
        UserSessionRepository(**{"user": user}).save()
        return login_token

    def get_login_token(self, user):
        expires_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=240)
        token = jwt.encode({'public_id': user.public_id, 'exp': expires_at}, Server().SECRET_KEY)
        return {"token": token, "expires_at": expires_at, "role": user.user_role.role}

    def get_logged_user(self, authData):
        userRepo = UserRepository()
        user = userRepo.get_by_publicid(authData['public_id'])
        if not user:
            raise BusinessException('Token inválido, usuário não encontrado.')
        return user

    def validate_signup_data(self, userData):
        #Verify properties
        if not userData['username']:
            raise BusinessException("O campo de usuário deve ser preenchido")
        elif not userData['password']:
            raise BusinessException("O campo de senha deve ser preenchido")
        elif not userData['trading_name']:
            raise BusinessException("O campo de razão social deve ser preenchido")
        elif not userData['document_id']:
            raise BusinessException("O campo de CNPJ deve ser preenchido")
