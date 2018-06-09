from flask import request, make_response, json
import app.new.model as model

def createnew():
    user = request.form['user']

    resp = model.createnew(user)
    return make_response(json.jsonify(data="ok"), 200)

def issuetoken(user):
    user = request.form['user']
    amount = request.form['amount']

    resp = model.issuetoken(user, amount)
    return make_response(json.jsonify(data="ok"), 200)
