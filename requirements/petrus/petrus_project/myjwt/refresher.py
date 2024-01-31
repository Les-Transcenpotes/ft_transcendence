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
    def payloadToJwt(payload: dict) -> Tuple[bool, str | list[str]]:
        try:
            token = jwt.encode(payload, JWT.privateKey, algorithm=JWT.privateKey)
        except Exception as e:
            return False, str(e)
        return True, token

    @staticmethod
    def jwtToPayload(token: str) -> Tuple[bool, dict | str]:
        try:
            payload = jwt.decode(token, JWT.publicKey, algorithms=[JWT.publicKey])
        except Exception as e:
            return False, str(e)
        return True, payload
