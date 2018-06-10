from flask import request, make_response, json
import app.action.model as model

def search():
    searcher = request.form['searcher']
    receiver = request.form['receiver']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']
    sentence_id = request.form['sentence_id']

    resp = model.search(searcher, receiver, source_lang, target_lang, sentence_id)
    return make_response(json.jsonify(data="ok"), 200)

def translate():
    user = request.form['user']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']
    sentence_id = request.form['sentence_id']

    resp = model.translate(user, source_lang, target_lang, sentence_id)
    return make_response(json.jsonify(data="ok"), 200)

