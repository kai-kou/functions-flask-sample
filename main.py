from flask import jsonify, make_response

def flask_json_response(request):
    return make_response(jsonify({'hoge': 'fuga'}))
