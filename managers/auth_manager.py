from datetime import datetime, timedelta

import jwt
from decouple import config
from flask import request, g
from flask_httpauth import HTTPTokenAuth
from jwt import ExpiredSignatureError, InvalidTokenError
from werkzeug.exceptions import Unauthorized

from models.user_models import UserModel


class AuthManager:
    MISSING_TOKEN_MESSAGE = "Missing token!"
    TOKEN_EXPIRED_MESSAGE = "Token expired!"
    INVALID_TOKEN_MESSAGE = "Invalid token!"
    TOKEN_LIFETIME_IN_HOURS = 2

    @classmethod
    def encode_token(cls, user):
        payload = {"sub": user.id,
                   "exp": datetime.utcnow() + timedelta(hours=cls.TOKEN_LIFETIME_IN_HOURS)
                   }
        return jwt.encode(payload, key=config("JWT_SECRET"), algorithm="HS256")

    @classmethod
    def decode_token(cls, token):
        if not token:
            raise Unauthorized(cls.MISSING_TOKEN_MESSAGE)
        try:
            payload = jwt.decode(token, key=config("JWT_SECRET"), algorithms=["HS256"])
            return {"id": payload["sub"]}

        except ExpiredSignatureError:
            raise Unauthorized(cls.TOKEN_EXPIRED_MESSAGE)
        except InvalidTokenError:
            raise Unauthorized(cls.INVALID_TOKEN_MESSAGE)


class Auth(HTTPTokenAuth):
    @staticmethod
    def login_optional(func):
        """Create current_user if request is authenticated"""

        def wrapper(*args, **kwargs):
            authorization_header = request.headers.get('Authorization')
            token = authorization_header[7:]
            if token:
                user_id, user_role = AuthManager.decode_token(token).values()
                user = UserModel.query.filter_by(id=user_id).first()
                g.flask_httpauth_user = user

            return func(*args, **kwargs)

        return wrapper


auth = Auth()


@auth.verify_token
def verify(token):
    user_id = AuthManager.decode_token(token)["id"]
    return UserModel.query.filter_by(id=user_id).first()
