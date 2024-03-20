from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from memory.models import Player


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
        data = request.GET
        players = []
        if 'ids' in data:
            ids = [int(id) for id in data['ids']]
            players = Player.objects.filter(id__in=ids)
        return JsonResponse({"Player": [e.to_dict() for e in players]})

    def post(self, request):
        data = request.data
        if not 'Id' in data:
            return JsonResponse({"Err": "no id provided"})

        player = Player()
        player.unique_id = data['Id']
        player.elo = 500
        player.save()
        return JsonResponse({"Player": player.to_dict()})

    def delete(self, request):
        return JsonResponse({"": ""})

    def patch(self, request):
        return JsonResponse({"": ""})

class userPlayerView(View):
    def get(self, request):
        return JsonResponse({"": ""})
