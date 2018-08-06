from services.sqlalchemy import BaseModel, db
from models.Item import Item


class ShoppingList(BaseModel):
    __tablename__ = 'shopping_list'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, nullable=False)
    store_name = db.Column(db.String(200), nullable=False)
    items = db.relationship(Item, backref=db.backref('shopping_list', lazy=True))