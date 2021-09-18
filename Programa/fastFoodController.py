from flask import Flask, jsonify, request

from repository.fastFoodRepository import *

app = Flask(__name__)


@app.route("/all", methods=["GET"])
def API_findAll():
    # Não está retornando a lista
    return jsonify(findAll())


@app.route("/<id>", methods=["GET"])
def API_findById(id):
    return jsonify(findById(id))


@app.route("/", methods=["POST"])
def API_save():
    obj = request.json
    return jsonify(save(obj))


@app.route("/<id>", methods=["DELETE"])
def API_delete(id):
    obj = delete(id)
    return jsonify(obj)


@app.route("/<id>", methods=["PUT"])
def API_update(id):
    obj = update(id, request.json)
    return jsonify(obj)


app.run(port=8080, debug=True)
