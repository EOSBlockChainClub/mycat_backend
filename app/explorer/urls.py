from flask import Blueprint
import app.explorer.controller as ctrl

explorer = Blueprint('explorer', __name__)

explorer.add_url_rule('/', view_func=ctrl.getWholeAct, methods=['GET'])
explorer.add_url_rule('/<user>', view_func=ctrl.getUserAct, methods=['GET'])
