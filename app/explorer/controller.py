from flask import request, make_response, json
import app.explorer.model as model

def getWholeAct():
    page = request.args.get("page", 1)

    resp = model.getWholeAction(page)
    return make_response(json.jsonify(data=resp), 200)

def getUserAct(user):
    page = request.args.get("page", 1)

    resp = model.getUserAction(user, page)
    return make_response(json.jsonify(data=resp), 200)
