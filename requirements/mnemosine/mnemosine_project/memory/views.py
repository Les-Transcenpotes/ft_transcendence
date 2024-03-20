from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


class tournamentView(View):
    def get(self, request):
        return JsonResponse({"": ""})

    def post(self, request):
        return JsonResponse({"": ""})

    def patch(self, request):
        return JsonResponse({"": ""})


class userTournamentView(View):
    def get(self, request):
        return JsonResponse({"": ""})


class matchView(View):
    def get(self, request):
        return JsonResponse({"": ""})

    def post(self, request):
        return JsonResponse({"": ""})


class userMatchView(View):
    def get(self, request):
        return JsonResponse({"": ""})


class playerView(View):
    def get(self, request):
        return JsonResponse({"": ""})

    def post(self, request):
        return JsonResponse({"": ""})

    def delete(self, request):
        return JsonResponse({"": ""})

    def patch(self, request):
        return JsonResponse({"": ""})

class userPlayerView(View):
    def get(self, request):
        return JsonResponse({"": ""})
