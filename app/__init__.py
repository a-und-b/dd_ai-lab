from flask import Flask
from .models import Base, engine


def create_app():
    app = Flask(__name__)
    Base.metadata.create_all(engine)

    from .app import app as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
