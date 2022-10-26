import db_manager as dbm

from flask import jsonify, request


def project_api_routes(endpoint):
    @endpoint.route('/')
    def home():
        return "Welcome to Only_viewable store!!"

    @endpoint.route('/stocks', methods=['GET'])
    def fn_1():  # getting items name
        res = dbm.get_items()
        return res

    @endpoint.route('/stocks/<string:name>', methods=['GET'])
    def fn_2(name):  # getting the items' info by its name
        res = dbm.get_item_info(name)
        res.pop("_id")
        return jsonify(res)

    @endpoint.route('/stocks/add', methods=['POST'])
    def fn_3():
        req_data = request.get_json()
        dbm.add_item(req_data['name'], req_data['price'], req_data['quantity'])
        return jsonify({'message': str(req_data['name']) + ' added to stocks'})

    @endpoint.route('/stocks/update', methods=['PUT'])
    def fn_4():
        req_data = request.get_json()
        dbm.update_stock(req_data['name'], req_data['price'], req_data['quantity'])
        return jsonify({'message': str(req_data['name']) + ' info updated'})

    @endpoint.route('/stocks/delete/<string:name>', methods=['DELETE'])
    def fn_5(name):
        dbm.delete_item(name)
        return jsonify({'message': str(name) + ' deleted'})

    return endpoint
