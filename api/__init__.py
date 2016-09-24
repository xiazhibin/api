from flask import Flask

app = Flask(__name__)

from weather import weather_bp

app.register_blueprint(weather_bp)


@app.route('/')
def index():
    return 'fuxk'


if __name__ == '__main__':
    app.run()