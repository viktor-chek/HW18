from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.model.genre import GenreSchema


ns_genre = Namespace('genres')          # Создание неймспейса


genre_schemas = GenreSchema(many=True)               # Создание экзмепляров схем
genre_schema = GenreSchema()


@ns_genre.route('/')
class DirectorsView(Resource):
    def get(self):
        all_genres = genre_service.get_all()

        return genre_schemas.dump(all_genres), 200


@ns_genre.route('/<int:pk>')
class DirectorView(Resource):
    def get(self, pk):
        genre = genre_service.get_one(pk)

        return genre_schema.dump(genre), 200
