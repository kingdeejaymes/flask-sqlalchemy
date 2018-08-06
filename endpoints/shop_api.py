from flask import Blueprint, request
from models.ShoppingList import ShoppingList
from services.utils import create_json_response
import logging

logging.getLogger().setLevel(logging.INFO)
shop = Blueprint('shop', __name__, url_prefix='/api/shoplist')


@shop.route('/all', methods=['GET'])
def get_all():
    shopping_lists = ShoppingList.all()

    return create_json_response(shopping_lists, is_list=True)


@shop.route('/create', methods=['POST'])
def create():
    req_body = request.get_json()
    shopping_list = ShoppingList(**req_body).save()
    return create_json_response(shopping_list.to_dict())