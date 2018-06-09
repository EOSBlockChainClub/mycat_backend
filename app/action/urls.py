from flask import Blueprint
import app.action.controller as ctrl

action = Blueprint('action', __name__)

action.add_url_rule('/search', view_func=ctrl.search, methods=['POST'])
action.add_url_rule('/confirm', view_func=ctrl.confirm, methods=['POST'])
action.add_url_rule('/inputtag', view_func=ctrl.inputtag, methods=['POST'])
action.add_url_rule('/original', view_func=ctrl.original, methods=['POST'])
action.add_url_rule('/translate', view_func=ctrl.translate, methods=['POST'])
