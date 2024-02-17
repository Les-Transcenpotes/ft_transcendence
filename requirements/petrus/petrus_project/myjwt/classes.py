class User:
    nick: str
    error : str
    is_autenticated : bool
    id : int

    def __init__(self, nick='', error='', is_autenticated=False, id=-1):
        self.nick = nick
        self.error = error
        self.is_autenticated = is_autenticated
        self.id = id

    def __str__(self):
        return f"{self.nick}, {self.id}, {self.is_autenticated}\n"

    def toDict(self):
        return {
                'nick': self.nick,
                'error': self.error,
                'id': self.id,
        }
