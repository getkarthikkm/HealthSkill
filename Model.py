from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields

ma = Marshmallow()
db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    has_provider = db.Column(db.Boolean, nullable=False)
    has_children = db.Column(db.Boolean, nullable=False)
    cover_type = db.Column(db.String(30), nullable=False)
    skill = db.Column(db.String(20))

    def __init__(self, name, postcode, age, gender, has_provider, has_children, marital_status, cover_type):
        self.name = name
        self.postcode = postcode
        self.age = age
        self.gender = gender
        self.has_provider = has_provider
        self.has_children = has_children
        self.marital_status = marital_status
        self.cover_type = cover_type


class CustomerSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    postcode = fields.Integer(required=True)
    age = fields.Integer(required=True)
    gender = fields.String(required=True)
    has_provider = fields.Boolean(required=True)
    has_children = fields.Boolean(required=True)
    marital_status = fields.String(required=True)
    cover_type = fields.String(required=True)
    skill = fields.String()
