from functools import wraps
from flask import request, jsonify
import hashlib

# Dummy users with hardcoded tokens
users = {
    "admin": "admin-token"
}

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token not in users.values():
            return jsonify({'message': 'Token is missing or invalid'}), 403
        return f(*args, **kwargs)
    return decorated_function
