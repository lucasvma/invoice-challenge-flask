from flask import request
from app.controllers import users


def initialize_routes(app):
    # endpoint to add user
    @app.route("/user", methods=["POST"])
    def add_user():
        return users.add_user(request)

    # endpoint to show all users
    @app.route("/user", methods=["GET"])
    def get_user():
        return users.get_user()

    # endpoint to get user detail by id
    @app.route("/user/<id>", methods=["GET"])
    def user_detail(user_id):
        return users.user_detail(user_id)

    # endpoint to update user
    @app.route("/user/<id>", methods=["PUT"])
    def user_update(user_id):
        return users.user_update(user_id, request)

    # endpoint to delete user
    @app.route("/user/<id>", methods=["DELETE"])
    def user_delete(user_id):
        return users.user_delete(user_id)
