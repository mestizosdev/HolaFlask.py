from flask import jsonify
from ..model.user import User
from flaskr.config.database import db
from flask import current_app


class UserService:
    @staticmethod
    def find_all():
        users = User.query.all()
        users_list = [{'id': user.id, 'username': user.username} for user in users]

        return jsonify(users_list)

    @staticmethod
    def find_by_id(id):
        user = User.query.get(id)

        if user is None:
            return None

        user_dict = {'id': user.id, 'username': user.username}

        return jsonify(user_dict)

    @staticmethod
    def save(data):
        try:
            user = User(username=data['username'], password=data['password'])
            db.session.add(user)
            db.session.commit()

            user_dict = {'id': user.id, 'username': user.username}

            return jsonify(user_dict)
        except Exception as e:
            current_app.logger.error(f'Error to save user {e}.')
            raise ValueError('Error to save user.')

    @staticmethod
    def update(id, data):
        user = User.query.get(id)
        user.username = data['username']
        user.password = data['password']
        db.session.commit()

        user_dict = {'id': user.id, 'username': user.username}

        return jsonify(user_dict)

    @staticmethod
    def delete(id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'User deleted'})
