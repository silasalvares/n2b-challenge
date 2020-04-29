from flask import Flask, request, jsonify

from .utils import make_json_webapi, make_json_response
from .dataset import DatasetHandler
from .schemas import FilterSchema, SearchResultSchema

webapi = make_json_webapi(__name__)

dataset_handler = DatasetHandler('winemag-data-130k-v2.csv')

@webapi.route('/', methods=['GET'])
def api_info():
    return jsonify({})

@webapi.route('/search/', methods=['POST'])
def search():
    request_data = FilterSchema().load(request.json)
    result = dataset_handler.filter(request_data)
    return make_json_response(data=SearchResultSchema().dump(result, many=True))
    