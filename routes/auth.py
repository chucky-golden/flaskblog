from flask import Blueprint
from views.auth import auth

auth_route = Blueprint('auth_route', __name__)

auth_route.add_url_rule('/login', view_func=auth.login, methods=['GET', 'POST'])
auth_route.add_url_rule('/register', view_func=auth.register, methods=['GET', 'POST'])
auth_route.add_url_rule('/dashboard', view_func=auth.dashboard, methods=['GET', 'POST'])
auth_route.add_url_rule('/viewpost', view_func=auth.viewpost, methods=['GET', 'POST'])
auth_route.add_url_rule('/viewcontact', view_func=auth.viewcontact, methods=['GET', 'POST'])
auth_route.add_url_rule('/editpost/<int:post_id>', view_func=auth.editpost, methods=['GET', 'POST'])
auth_route.add_url_rule('/deletepost/<int:post_id>', view_func=auth.deletepost)
auth_route.add_url_rule('/deletecontact/<int:post_id>', view_func=auth.deletecontact)
auth_route.add_url_rule('/logout', view_func=auth.logout)
