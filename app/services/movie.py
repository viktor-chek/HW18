class MovieService:
    """Сервис для работы с Movie"""
    def __init__(self, dao):
        self.dao = dao

    def get_all(self, req_body):
        return self.dao.get_all(req_body)

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def update(self, data, mid):
        movie = self.get_one(mid)

        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']

        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)

    def create(self, data):
        return self.dao.create(data)
