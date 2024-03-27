from django.http import JsonResponse
from django.views.i18n import View


class tournamentView(View):
    def get(self, request):
        return JsonResponse({"": ""})


