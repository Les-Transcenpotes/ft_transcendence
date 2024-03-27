from datetime import datetime, timedelta
from jwt import encode, decode



from .var import public_key
from .var import private_key
from .var import algo


class JWT:
    publicKey = public_key   # replace os.environ['PUBLIC_KEY']
    privateKey = private_key  # replace os.environ['PRIVATE_KEY']
    algo = algo
    expiration_acccess_token = timedelta(minutes=15)
    expiration_refresh_token = timedelta(days=1)

    @staticmethod
    def payloadToJwt(payload: dict, key: str):
        """
        TODO : mettre les key dans l'env
        key is the str :
            -- access -> JWT.privateKey
            -- refresh -> JWT.refreshPublicKey
        Return True and the token | False and the error
        """
        return encode(payload, key, algorithm=JWT.algo)

    @staticmethod
    def jwtToPayload(token: str, key: str):
        """
        token is the jwt
        TODO : mettre les key dans l'env
        key is the str :
            -- access -> JWT.publicKey
            -- refresh -> JWT.refreshPublicKey
        Return True and the payload | False and the error
        """
        return decode(token, key, algorithms=[JWT.algo])

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
