from flask import Blueprint, request
from project.services.utils import create_json_response
from project.models.ShoppingList import ShoppingList
from project.models.Item import Item
import logging

logging.getLogger().setLevel(logging.INFO)
shop = Blueprint('shop', __name__, url_prefix='/api/shoplist')


@shop.route('/all', methods=['GET'])
def get_all():
    shopping_lists = ShoppingList.all()

    return create_json_response(shopping_lists, is_list=True)


@shop.route('/find_by', methods=['GET'])
def get_by_field():
    title = request.args.get('title')
    if title is None:
        create_json_response("Title is missing", 404)

    shopping_list = ShoppingList.get_by_wildcard(ShoppingList.title, title)

    if shopping_list is None:
        return create_json_response("Shopping List with title: {}".format(title) + " is not in the Database", 404)

    return create_json_response(shopping_list, is_list=True)


@shop.route('/create', methods=['POST'])
def create():
    req_body = request.get_json()
    shopping_list = ShoppingList(**req_body).save()
    return create_json_response(shopping_list.to_dict())


@shop.route('/<string:sl_id>/add_item/<string:item_id>', methods=['PUT'])
def add_item(sl_id, item_id):
    item = Item.get(int(item_id))
    if item is None:
        return create_json_response('Item with ID: {}'.format(item_id) + ' cannot be found', 404)

    shopping_list = ShoppingList.get(int(sl_id))
    if shopping_list is None:
        return create_json_response('Shopping List with ID: {}'.format(sl_id) + ' cannot be found', 404)

    shopping_list.items.append(item)
    shopping_list.update()

    items = shopping_list.items
    shopping_list_dict = shopping_list.to_dict()
    shopping_list_dict['items'] = []

    for item in items:
        shopping_list_dict['items'].append(item.to_dict())

    return create_json_response(shopping_list_dict)


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


@shop.route('/delete/<string:sl_id>', methods=['DELETE'])
def delete(sl_id):
    shopping_list = ShoppingList.get(int(sl_id))

    if shopping_list is None:
        return create_json_response("Shopping List with ID: {}".format(sl_id) + " is not in the Database", 404)

    shopping_list.delete()
    return create_json_response("Shopping List with ID: {}".format(sl_id) + " was successfully deleted")