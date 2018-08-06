from flask import jsonify


def create_json_response(response, status=200, is_list=False):

    if is_list:
        items = []
        for i in response:
            items.append(i.to_dict())
        response = items

    return jsonify(
        status=status,
        data=response
    )

