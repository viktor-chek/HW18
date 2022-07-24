from app.setup_db import db
from marshmallow import Schema, fields


class Genre(db.Model):
    """Создание модели для таблицы genre"""
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """Создание схемы сериализации/десериализации для genre"""
    id = fields.Int()
    name = fields.Str()
