from datetime import datetime, timedelta
from typing import Tuple
from jwt import encode, decode, ExpiredSignatureError



from .var import public_key
from .var import private_key
from .var import algo
import os


class JWT:
    publicKey = public_key   # replace os.environ['PUBLIC_KEY']
    privateKey = private_key  # replace os.environ['PRIVATE_KEY']
    algo = algo
    expiration_acccess_token = timedelta(minutes=15)
    expiration_refresh_token = timedelta(days=1)

    @staticmethod
    def payloadToJwt(payload: dict, key: str) -> Tuple[bool, str]:
        """
        TODO : mettre les key dans l'env
        key is the str :
            -- access -> JWT.privateKey
            -- refresh -> JWT.refreshPublicKey
        Return True and the token | False and the error
        """
        try:
            token = encode(payload, key, algorithm=JWT.algo)
        except Exception as e:
            return False, str(e)
        return True, token

    @staticmethod
    def jwtToPayload(token: str, key: str) -> str | dict:
        """
        token is the jwt
        TODO : mettre les key dans l'env
        key is the str :
            -- access -> JWT.publicKey
            -- refresh -> JWT.refreshPublicKey
        Return True and the payload | False and the error
        """
        try:
            payload = decode(token, key, algorithms=[JWT.algo])
        except BaseException as e:
            return e.__str__()
        return payload

    @staticmethod
    def peremptionDict() -> dict:
        peremption = datetime.utcnow() + timedelta(minutes=15)
        return {'exp': peremption}

    @staticmethod
    def verifJWT(str, key) -> str | dict:
        content = JWT.jwtToPayload(str, key)
        if isinstance(content, dict):
            del content['peremption']
            return content
        return content

    @staticmethod
    def toPayload(object) -> dict:
        return object.toDict() | JWT.peremptionDict()

    @staticmethod
    def objectToAccessToken(object):
        return JWT.payloadToJwt(JWT.toPayload(object), JWT.privateKey)

    @staticmethod
    def objectToRefreshToken(object):
        return JWT.payloadToJwt(object.toDict() | {'exp': (datetime.utcnow() + timedelta(days=1))}, JWT.privateKey)