from django.db import Error
from django.http import HttpRequest
from shared.jwt import JWT
from .var import public_key
from .common_classes import User
import os



class JWTIdentificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        key = public_key
        # key = os.environ.get('PUBLIC_KEY_JWT')
        if not key:
            raise Error("publicKey is not defined")
        self.publicKey = key

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        autorisationJWT = request.META.get('aut')
        if not autorisationJWT:
            request.user = User(error="No JWT provided")
            return None

        # user = User(nick='me', id=-2)
        # autorisationJWT = JWT.objectToAccessToken(user)

        decodedJWT = JWT.jwtToPayload(autorisationJWT, self.publicKey)
        if isinstance(decodedJWT, str):
            request.user = User(error=decodedJWT)
            return None

        request.user = User(nick=decodedJWT.get('nick'),
                            id=decodedJWT.get('id'),
                            is_autenticated=True)

        return None
