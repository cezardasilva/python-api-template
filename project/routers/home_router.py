import json
from flask import Blueprint, request, make_response, jsonify

home_route = Blueprint('home_route', __name__)
@home_route.route("/", methods=["GET"])
def home():
    return make_response('<h1>API - v1</h1>', 200)
