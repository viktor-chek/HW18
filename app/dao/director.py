from app.dao.model.director import Director


class DirectorDAO:
    """Класс для работы с базой для сущности Director"""
    def __init__(self, session):
        self.session = session

    def get_all(self):

        return self.session.query(Director).all()

    def get_one(self, did):

        return self.session.query(Director).get(did)
