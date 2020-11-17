

import json
from flask import Flask, make_response, jsonify


app = Flask("json_render")

@app.route("/json/1")
def json_api():
    pessoas = [{"nome": "Bruno Rocha"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]
    response = make_response(json.dumps(pessoas))
    response.content_type = "application/json"
    # ou
    # response.headers['Content-Type'] = "application/json"
    return response

@app.route("/json/2")
def json_api2():
    pessoas = [{"nome": "milena"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]
    return json.dumps(pessoas), 200, {"Content-Type": "application/json"}

@app.route("/json/3")
def json_api3():
    pessoas = jsonify([{"nome": "alice voga"},
                       {"nome": "Arjen Lucassen"},
                       {"nome": "Anneke van Giersbergen"},
                       {"nome": "Steven Wilson"}])
    return pessoas



app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)
