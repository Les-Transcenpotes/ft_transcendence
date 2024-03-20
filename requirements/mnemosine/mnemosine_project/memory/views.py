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
        data = request.data
        if not 'Id' in data:
            return JsonResponse({"Err": "no id provided"})
        try:
            player = Player.objects.get(unique_id=data['id'])
        except:
            return JsonResponse({"Err": "no player for the id"})
        return JsonResponse({"Player suppressed": True})

    def patch(self, request):
        data = request.data
        if not 'Id' in data:
            return JsonResponse({"Err": "no id provided"})
        try:
            player = Player.objects.get(unique_id=data['id'])
        except:
            return JsonResponse({"Err": "no player for the id"})
        if not 'Elo' in data:
            return JsonResponse({"Err": "no elo provided"})
        player.elo = data['Elo']
        player.update()
        return JsonResponse({"Player updated": player.to_dict()})

class userPlayerView(View):
    def get(self, request):
        players = []
        error = []
        return_json = {}
        data = request.GET.getlist('players')
        try:
            ids = [int(id) for id in data]
        except:
            return JsonResponse({"Err": "wrong query params provided"})

        for id in ids:
            player = Player.objects.filter(unique_id = id).first()
            if player is not None:
                players.append(player)
            else:
                error.append(id)

        return_json |= {"Player": [e.to_dict() for e in players]}
        if len(error) != 0:
            return_json |= {"Warn": 'unknown id',
                            "Unknown": error}

        return JsonResponse(return_json)
