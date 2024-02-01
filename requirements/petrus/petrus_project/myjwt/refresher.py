from datetime import datetime, timedelta, timezone
from typing import Tuple
import jwt

from keys.publickey import public_key
from keys.privatekey import private_key
from keys.algo import algo
import os

class JWT():
    publicKey = public_key   # replace os.environ['PUBLIC_KEY']
    privateKey = private_key # replace os.environ['PRIVATE_KEY']
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
        try:
            token = jwt.encode(payload, key, algorithm=JWT.algo)
        except Exception as e:
            return False, str(e)
        return True, token

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
        try:
            payload = jwt.decode(token, key, algorithms=[JWT.algo])
        except Exception as e:
            return False, str(e)
        return True, payload
