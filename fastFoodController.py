from flask import Flask, jsonify, request

import repository.fastFoodRepository as repo

app = Flask(__name__)

repo.setRepository()  # Create a dataBase if not exists


@app.route("/all", methods=["GET"])
def API_findAll():
    # Não está retornando a lista
    return jsonify(repo.findAll())


@app.route("/<id>", methods=["GET"])
def API_findById(id):
    return jsonify(repo.findById(id))


@app.route("/", methods=["POST"])
def API_save():
    obj = request.json
    return jsonify(repo.save(obj))


@app.route("/<id>", methods=["DELETE"])
def API_delete(id):
    obj = repo.delete(id)
    return jsonify(obj)


@app.route("/<id>", methods=["PUT"])
def API_update(id):
    obj = repo.update(id, request.json)
    return jsonify(obj)


app.run(port=8080, debug=True)
