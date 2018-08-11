from project.services.sqlalchemy import BaseModel, db
from sqlalchemy import ForeignKey
from project.models.Item import Item
import datetime

association_table = db.Table('association', db.Model.metadata,
                             db.Column('shopping_list_id', db.Integer, ForeignKey('shopping_list.id')),
                             db.Column('item_id', db.Integer, ForeignKey('item.id'))
)


class ShoppingList(BaseModel):
    __tablename__ = 'shopping_list'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, nullable=False)
    store_name = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    items = db.relationship('Item', secondary=association_table, backref=db.backref('shopping_list', lazy=True))

    @classmethod
    def get_by_item_id(cls, item_id):
        return db.session.query(cls).join(Item, cls.items).filter(Item.item_ref_id == item_id)

    @classmethod
    def get_by_item_name_wildcard(cls, item_name):
        return db.session.query(cls).join(Item, cls.items)\
                 .filter(Item.item_id.name.like('%' + item_name + '%')).all()
