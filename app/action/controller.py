from flask import request, make_response, json
import app.action.model as model

def search():
    user = request.form['user']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']
    sentence_id = request.form['sentence_id']

    resp = model.search(user, source_lang, target_lang, sentence_id)
    return make_response(json.jsonify(data="ok"), 200)

def confirm():
    user = request.form['user']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']
    sentence_id = request.form['sentence_id']

    resp = model.confirm(user, source_lang, target_lang, sentence_id)
    return make_response(json.jsonify(data="ok"), 200)

def inputtag():
    user = request.form['user']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']
    sentence_id = request.form['sentence_id']
    tag_id = request.form['tag_id']

    resp = model.inputtag(user, source_lang, target_lang, sentence_id, tag_id)
    return make_response(json.jsonify(data="ok"), 200)

def original():
    user = request.form['user']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']
    sentence_id = request.form['sentence_id']

    resp = model.original(user, source_lang, target_lang, sentence_id)
    return make_response(json.jsonify(data="ok"), 200)

def translate():
    user = request.form['user']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']
    sentence_id = request.form['sentence_id']

    resp = model.translate(user, source_lang, target_lang, sentence_id)
    return make_response(json.jsonify(data="ok"), 200)

