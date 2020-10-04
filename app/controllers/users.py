from flask import jsonify
from app.models.users import user_schema, users_schema, User
# from app.database.db import session


def add_user(request):
    username = request.json['username']
    email = request.json['email']

    new_user = User(username, email)

    user_schema.add(new_user)
    user_schema.commit()

    return jsonify(new_user)


def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)

    return jsonify(result)


def user_detail(user_id):
    user = User.query.get(user_id)
    return user_schema.jsonify(user)


def user_update(user_id, request):
    user = User.query.get(user_id)
    username = request.json['username']
    email = request.json['email']

    user.email = email
    user.username = username

    user_schema.commit()

    return user_schema.jsonify(user)


def user_delete(user_id):
    user = User.query.get(user_id)
    user_schema.delete(user)
    user_schema.commit()

    return user_schema.jsonify(user)
