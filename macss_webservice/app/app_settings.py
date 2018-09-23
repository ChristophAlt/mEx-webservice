from sanic import Blueprint

API_VERSION = '0.1'
URL_BASE = '/api/' + API_VERSION

app_endpoints = Blueprint('app_endpoints')
