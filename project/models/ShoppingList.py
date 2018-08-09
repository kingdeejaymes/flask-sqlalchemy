from project.services.sqlalchemy import BaseModel, db
from project.models.Item import Item


class ShoppingList(BaseModel):
    __tablename__ = 'shopping_list'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, nullable=False)
    store_name = db.Column(db.String(200), nullable=False)
    items = db.relationship('Item', backref=db.backref('shopping_list', lazy=True))

    @classmethod
    def get_by_item_id(cls, item_id):
        return db.session.query(cls).join(Item, cls.items).filter(Item.id == item_id)
