from django.db import Error
from django.http import HttpRequest, JsonResponse
from shared.jwt_management import JWT
from .var import public_key
from .common_classes import User
import os
import json


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
        if not 'Aut' in request.data:
            request.user = User(error="No JWT provided")
            return None

        autorisationJWT = request.data['Aut']

        decodedJWT = JWT.jwtToPayload(autorisationJWT, self.publicKey)

        if isinstance(decodedJWT, str):
            request.user = User(error=decodedJWT)
            return None

        request.user = User(nick=decodedJWT.get('nick'),
                            id=decodedJWT.get('id'),
                            is_autenticated=True)

        return None


class ensureIdentificationMiddleware:
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
        if not request.user.is_autenticated:
            return JsonResponse({"Err": request.user.error})
        return None


class RawJsonToDataGetMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            request.data = json.loads(request.body.decode('utf-8'))
        except BaseException as e:
            request.data = {"Err": e}
        return None
