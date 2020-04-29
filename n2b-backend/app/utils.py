from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import default_exceptions

def make_json_response(success=True, msg='', data={}):
    return jsonify({
        'success': success,
        'msg': msg,
        'data': data
    })

def make_json_webapi(import_name, **kwargs):
    webapi = Flask(import_name, **kwargs)

    def make_json_error(ex):
        error = str(ex)
        if not str(error):
            error = 'Internal Server Error' 
        error += ' ' + str(type(ex))
        return make_json_response(success=False, msg=error)

    for exception in default_exceptions.items():
        webapi.register_error_handler(exception[0], make_json_error)

    webapi.register_error_handler(Exception, make_json_error)

    @webapi.after_request
    def set_content_type(response):
        response.headers["Content-Type"] = "application/json"
        return response

    CORS(webapi)
    return webapi