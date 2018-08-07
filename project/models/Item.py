from project.services.sqlalchemy import BaseModel, db
from sqlalchemy import ForeignKey


class Item(BaseModel):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer)
    shopping_list_id = db.Column(db.Integer, ForeignKey('shopping_list.id'))