from flask import Blueprint
from views.basic import basic

basic_route = Blueprint('basic_route', __name__)

# if you want to add other request other than POST and GET do this
# basic_route.add_url_rule('', view_func=basic.index, methods=['GET', 'POST', 'PUT', 'DELETE'])

basic_route.add_url_rule('', view_func=basic.index)
basic_route.add_url_rule('/about', view_func=basic.about)
basic_route.add_url_rule('/contact', view_func=basic.contact, methods=['GET', 'POST'])
basic_route.add_url_rule('/category', view_func=basic.category)
basic_route.add_url_rule('/single/<int:post_id>', view_func=basic.single)
