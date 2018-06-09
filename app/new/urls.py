from flask import Blueprint
import app.new.controller as ctrl

new = Blueprint('new', __name__)

new.add_url_rule('/createnew', view_func=ctrl.createnew, methods=['POST'])
new.add_url_rule('/issuetoken', view_func=ctrl.issuetoken, methods=['POST'])
