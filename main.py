from flask import Flask
from flask_restx import Api

from app.setup_db import db
from app.config import Config
from app.views.movie.movie import ns_movie
from app.views.director.director import ns_director
from app.views.genre.genre import ns_genre


# функция создания основного объекта app
def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    configure_app(application)
    application.app_context().push()
    return application


# функция настроек приложения
def configure_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(ns_movie)
    api.add_namespace(ns_director)
    api.add_namespace(ns_genre)


if __name__ == '__main__':
    app = create_app(Config())
    app.run(host="127.0.0.1", port=5000)
