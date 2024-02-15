class JWTMiddleware:
    def __init__(self, get_response):
        print("init of the middleware")
        self.get_response = get_response

    def __call__(self, request):
        print("I was called")
        response = self.get_response(request)
        return response

