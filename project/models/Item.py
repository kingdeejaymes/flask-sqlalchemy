from project.services.sqlalchemy import BaseModel, db


class Item(BaseModel):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    fixed_quantity = db.Column(db.Integer, default=0)
    updated_quantity = db.Column(db.Integer, default=0)
