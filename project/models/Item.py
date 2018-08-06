from project.services.sqlalchemy import BaseModel, db


class Item(BaseModel):
    __tablename__ = 'item'

    name = db.Column(db.String(100), primary_key=True)
    quantity = db.Column(db.Integer)
    shopping_list_id = db.Column(db.Integer, db.ForeignKey('shopping_list.id'), nullable=True)