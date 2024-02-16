from django.db import Error
from django.http import HttpRequest, JsonResponse
from myjwt.jwt import JWT
from keys import publickey
import os

class RefreshMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        key = publickey.public_key
        # key = os.environ.get('PUBLIC_REFRESH_KEY_JWT')
        if not key:
            raise Error("publicKey is not defined")
        self.publicKey = key

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        ensure_JWT = getattr(view_func, "_ensure_refresh_token", False)
        if (ensure_JWT == False):
            return None
        autorisationJWT = request.META.get('ref')
        if not autorisationJWT:
            return JsonResponse({"error": "Missing JWT"}, status=401)
        decodedJWT = JWT.jwtToPayload(autorisationJWT, self.publicKey)
        if decodedJWT is str:
            return JsonResponse({"error": decodedJWT}, status=401)
        return None
