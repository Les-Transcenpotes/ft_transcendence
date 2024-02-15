from django.db import Error
from django.http import HttpRequest, JsonResponse
from myjwt.jwt import JWT
from keys import publickey
import os

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        key = publickey.public_key
        # key = os.environ.get('PUBLIC_KEY_JWT')
        if not key:
            raise Error("publicKey is not defined")
        self.publicKey = key


    def __call__(self, request: HttpRequest):

        autorisationJWT = request.META.get('aut')

        if not autorisationJWT:
            return JsonResponse({"error": "Missing JWT"}, status=401)

        decodedJWT = JWT.jwtToPayload(autorisationJWT, self.publicKey)
        if decodedJWT is str:
            return JsonResponse({"error": decodedJWT}, status=401)

        response = self.get_response(request)
        return response
