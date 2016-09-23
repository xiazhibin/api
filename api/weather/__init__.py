from flask import Blueprint

weather_bp = Blueprint('weather', __name__, url_prefix='/api/weather')


@weather_bp.route('/')
def index():
    return 'fuxk'