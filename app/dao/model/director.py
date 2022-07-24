from marshmallow import Schema, fields
from app.setup_db import db


class Director(db.Model):
    """Создание модели для таблицы director"""
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    """Создание схемы сериализации/десериализации для director"""
    id = fields.Int()
    name = fields.Str()

