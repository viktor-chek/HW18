from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.model.director import DirectorSchema


ns_director = Namespace('directors')          # Создание неймспейса


director_schemas = DirectorSchema(many=True)               # Создание экзмепляров схем
director_schema = DirectorSchema()


@ns_director.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()

        return director_schemas.dump(all_directors), 200


@ns_director.route('/<int:pk>')
class DirectorView(Resource):
    def get(self, pk):
        director = director_service.get_one(pk)

        return director_schema.dump(director), 200
