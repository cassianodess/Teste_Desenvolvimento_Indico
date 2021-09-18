from flask import Flask, jsonify, make_response, request

import service.fastFoodService as service

app = Flask(__name__)


service.setRepository()  # Create a dataBase if not exists


@app.route("/all", methods=["GET"])
def API_findAll():
    # Não está retornando a lista
    return jsonify(service.findAll())


@app.route("/<id>", methods=["GET"])
def API_findById(id):

    try:
        return jsonify(service.findById(id))
    except:
        return make_response(f"Id '{id}' not found!", 404)


@app.route("/", methods=["POST"])
def API_save():
    obj = request.get_json()
    if service.verifyColumns(obj):
        return jsonify(service.save(obj))
    else:
        return make_response("Invalid Body! Missing field(s)", 401)


@app.route("/<id>", methods=["DELETE"])
def API_delete(id):

    try:
        return jsonify(service.delete(id))

    except:
        return make_response(f"Id '{id}' not found!", 404)


@app.route("/<id>", methods=["PUT"])
def API_update(id):
    obj = request.get_json()

    if service.verifyColumns(obj):
        try:
            jsonify(service.findById(id))
            try:
                return jsonify(service.update(id, obj))
            except:
                return make_response(f"Id '{id}' not found!", 404)
        except:
            return make_response(f"Id '{id}' not found!", 404)

    else:
        return make_response(f"Invalid Body!", 401)


app.run(port=8080)
