from django.utils.deprecation import MiddlewareMixin


class DisableCsrfCheck(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
