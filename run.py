from flask import Flask, Blueprint
from app.controllers.weatherController import weatherRoute

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return "Hello World"
    return app

app = create_app()
app.register_blueprint(weatherRoute)
app.run(debug=True, port=5000)

