import jwt
from project.config import Server
from functools import wraps
from flask import Flask, make_response, jsonify, request

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response(jsonify({'message': 'Token is invalid'}), 401)
        try:
            data = jwt.decode(token, Server().SECRET_KEY)
        except Exception as ex:
            return make_response(jsonify({'message': 'Token is invalid'}), 401)

        return f(data, *args, **kwargs)
    return decorated
