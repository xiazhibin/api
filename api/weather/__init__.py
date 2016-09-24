# coding=utf-8
from flask import Blueprint, make_response
import requests
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

weather_bp = Blueprint('weather', __name__, url_prefix='/api/weather')

weather_url_prefix = 'http://api.map.baidu.com/telematics/v3/weather?location=#&output=json&ak=ZLUIqERpIcPUhOK9KVCUdNBa2upZttv8'


@weather_bp.route('/<string:city>')
def index(city):
    url = weather_url_prefix.replace('#', city)
    r = requests.get(url)
    response = make_response(r.content)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
