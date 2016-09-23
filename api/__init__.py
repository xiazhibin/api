from flask import Flask


app = Flask(__name__)


from weather import weather_bp
app.register_blueprint(weather_bp)
