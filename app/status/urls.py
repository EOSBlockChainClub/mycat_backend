from flask import Blueprint
import app.status.controller as ctrl

status = Blueprint('status', __name__)

status.add_url_rule('/token/<user>', view_func=ctrl.token, methods=['GET'])
status.add_url_rule('/point/<user>', view_func=ctrl.point, methods=['GET'])
