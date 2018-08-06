from flask import Flask
from services.sqlalchemy import db
from endpoints.shop_api import shop
import logging


logging.getLogger().setLevel(logging.DEBUG)
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/shoplistdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(shop)
app.config.update(DEBUG=True)

db.init_app(app)
db.create_all(app=app)
