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


@shop.route('/update/<string:sl_id>', methods=['PUT'])
def update(sl_id):
    req_body = request.get_json()
    shopping_list = ShoppingList.get(int(sl_id))

    if shopping_list is None:
        return create_json_response("Shopping List with ID: {}".format(sl_id) + " is not in the Database", 404)

    shopping_list.title = req_body['title']
    shopping_list.store_name = req_body['store_name']
    shopping_list.update()

    return create_json_response(shopping_list.to_dict())