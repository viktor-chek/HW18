from app.dao.model.genre import Genre


class GenreDAO:
    """Класс для работы с базой для сущности Genre"""
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)
