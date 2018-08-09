from flask import jsonify


def create_json_response(response, status=200, is_list=False):

    if is_list:
        items = []
        for i in response:
            items.append(parse_items_response(i))
        response = items

    return jsonify(
        status=status,
        data=response
    )


def parse_items_response(shopping_list):
    items = shopping_list.items
    shopping_list_dict = shopping_list.to_dict()
    shopping_list_dict['items'] = []

    for item in items:
        shopping_list_dict['items'].append(item.to_dict())

    return shopping_list_dict

