from flask import request, make_response, json
import app.status.model as model

def token(user):
    resp = model.getToken(user)
    return make_response(json.jsonify(data=resp), 200)

def point(user):
    resp = model.getPoint(user)
    return make_response(json.jsonify(data=resp), 200)
