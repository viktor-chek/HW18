from app.dao.model.movie import Movie


class MovieDAO:
    """Класс для работы с базой для сущности Movie"""
    def __init__(self, session):
        self.session = session

    def get_all(self, req_body):
        if req_body.get('director_id'):
            return self.session.query(Movie).filter(Movie.director_id == req_body.get('director_id')).all()
        elif req_body.get('genre_id'):
            return self.session.query(Movie).filter(Movie.genre_id == req_body.get('genre_id')).all()
        elif req_body.get('year'):
            return self.session.query(Movie).filter(Movie.year == req_body.get('year')).all()

        return self.session.query(Movie).all()

    def get_one(self, mid):

        return self.session.query(Movie).get(mid)

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        dlt_movie = self.get_one(mid)
        self.session.delete(dlt_movie)
        self.session.commit()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie
