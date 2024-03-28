from django.http import HttpRequest


def report_error(request: HttpRequest, error):
    print(f'An error occured : {error}')


