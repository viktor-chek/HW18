from flask import request, jsonify
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.model.movie import MovieSchema


ns_movie = Namespace('movies')          # Создание неймспейса


schema_movies = MovieSchema(many=True)               # Создание экзмепляров схем
schema_movie = MovieSchema()


@ns_movie.route('/')
class MoviesView(Resource):
    def get(self):
        request_body = request.args

        all_movies = movie_service.get_all(request_body)

        return schema_movies.dump(all_movies), 200

    def post(self):
        datas = request.json
        new_movie = movie_service.create(datas)
        response = jsonify(schema_movie.dump(new_movie))
        response.status_code = 201
        response.headers['Location'] = new_movie.id

        return response


@ns_movie.route('/<int:pk>')
class MovieView(Resource):
    def get(self, pk):
        movie = movie_service.get_one(pk)

        return schema_movie.dump(movie), 200


    def put(self, pk):
        body_request = request.json
        movie_service.update(body_request, pk)

        return "", 204


    def delete(self, pk):
        movie_service.delete(pk)

        return "", 204
