from flask import jsonify


class UserService:
    @staticmethod
    def find_all():
        from ..model.user import User

        users = User.query.all()
        users_list = [{'id': user.id, 'username': user.username} for user in users]

        return jsonify(users_list)

    @staticmethod
    def find_by_id(id):
        from ..model.user import User

        user = User.query.get(id)

        if user is None:
            return None

        user_dict = {'id': user.id, 'username': user.username}

        return jsonify(user_dict)

    @staticmethod
    def save(data):
        from ..model.user import User
        from flaskr import db

        user = User(username=data['username'], password=data['password'])
        db.session.add(user)
        db.session.commit()

        user_dict = {'id': user.id, 'username': user.username}

        return jsonify(user_dict)

    @staticmethod
    def update(id, data):
        from ..model.user import User
        from flaskr import db

        user = User.query.get(id)
        user.username = data['username']
        user.password = data['password']
        db.session.commit()

        user_dict = {'id': user.id, 'username': user.username}

        return jsonify(user_dict)

    @staticmethod
    def delete(id):
        from ..model.user import User
        from flaskr import db

        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'User deleted'})
