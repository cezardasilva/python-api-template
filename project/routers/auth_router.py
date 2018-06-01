import json
from flask import Blueprint, request
from project.config import Server

from project.services.authorization_service import AuthorizationService

auth_route = Blueprint('auth_route', __name__)

server = Server()
basePath = server.get_base_path()
AUTH_PREFIX = basePath + '/auth'

@auth_route.route(AUTH_PREFIX + "/signup", methods=["POST"])
def signup():
    """
    Signup user
    ---
      tags:
        - Auth
      summary: Register a new user
      description: 'Receveis all data to create a new user'
      operationId: signup
      consumes:
        - application/json
      produces:
        - application/json
      parameters:
        - name: user
          in: body
          description: The user name for login
          required: true
          schema:
            type: object
            required:
                - username
            properties:
                username:
                    type: string
                password:
                    type: string
                password_retype:
                    type: string
                trading_name:
                    type: string
                document_id:
                    type: string
                profile:
                    type: string
                publisher:
                    type: string
      responses:
        '405':
          description: Invalid inp
    """
    params = json.loads(request.data)
    authService = AuthorizationService()
    result = authService.do_signup(params)
    return result

@auth_route.route(AUTH_PREFIX + "/login", methods=["POST"])
def login():
    """
    Endpoint to login an user.
    ---
      tags:
        - Auth
      summary: Login user and get JWT token
      description: 'Receives username and password to authenticate user'
      operationId: login
      consumes:
        - application/json
      produces:
        - application/json
      security:
        - basicAuth: []
      responses:
        '405':
          description: Invalid inp
    """
    auth = request.authorization
    authService = AuthorizationService()
    result = authService.do_login(auth)
    return result
