from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt


def roles_required(required_roles):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            # Get the current user's roles from the JWT claims
            jwt = get_jwt()
            roles = jwt.get('roles')

            # Check if the user has at least one of the required roles
            if any(role in roles for role in required_roles):
                return fn(*args, **kwargs)
            else:
                return {'message': 'Access forbidden'}, 403

        return wrapper

    return decorator
