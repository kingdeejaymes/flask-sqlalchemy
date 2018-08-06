import datetime
from flask_sqlalchemy import SQLAlchemy
import logging

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    meta_created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    meta_updated_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

    @classmethod
    def get(cls, pkey):
        return db.session.query(cls).get(pkey)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def refresh(self):
        db.session.refresh(self)

    def to_dict(self):
        return dict((k, getattr(self, k)) for k in self.__table__.c.keys())