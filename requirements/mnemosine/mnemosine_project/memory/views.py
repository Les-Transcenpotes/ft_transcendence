from django.http import JsonResponse
from django.views import View

from memory.models import Tournament, Game, Player

def request_get_all(ids_str, key_name, model):
    return_json = {}
    try :
        ids = [int(id) for id in ids_str]
    except TypeError:
        return {"Err": "wrong query params provided"}
    querylist = model.objects.filter(id__in=ids)

    if len(ids) != len(querylist):
        return_json |= {"Warn": "invalid ids provided"}
    return_json |= {key_name: [queryobject.to_dict() for queryobject in querylist]}
    return return_json

class tournamentView(View):
    def get(self, request, id: int = 0):
        return_json = {}

        queries = request.GET.getlist('query')

        data = request.GET.getlist('tournaments')
        return_json |= request_get_all(data, "Tournaments", Tournament)
        return JsonResponse(return_json)

    def post(self, request, id: int = 0):
        data = request.data
        return JsonResponse({})


class gameView(View):
    def get(self, request):
        return_json = {}

        data = request.GET.getlist('games')
        return_json |= request_get_all(data, "Games", Game)
        return JsonResponse(return_json)

    def post(self, request):
        data = request.data
        info_array = []
        for key in ('P1', 'Score-p1', 'P2', 'Score-p2'):
            if key not in data:
                return JsonResponse({"Err": f'missing value {key}'})
            try:
                info_array.append(int(data[key]))
            except BaseException:
                return JsonResponse({"Err": "bad body content"})
        new_game = Game()
        try:
            new_game.player1 = Player.objects.get(unique_id=info_array[0])
        except BaseException:
            return JsonResponse({"Err": "Player does not exist"})
        new_game.score1 = info_array[1]
        try:
            new_game.player2 = Player.objects.get(unique_id=info_array[2])
        except BaseException:
            return JsonResponse({"Err": "Player does not exist"})
        new_game.score2 = info_array[3]
        try:
            new_game.save()
        except BaseException:
            return JsonResponse({"Err": "unexpected error ocured"})
        return JsonResponse({})


class playerView(View):
    def get(self, request, id: int = 0, ressource: str = "all"):
        return_json = {}

        queries = request.GET.getlist('query')

        if 'perso' in queries:
            try:
                personal_player = Player.objects.get(id=request.user.id)
                return_json |= {"Perso" : personal_player.to_dict()}
            except BaseException as e:
                return_json |= {"Err": e.__str__()}

        if 'friends' in queries:
            try:
                # request to alfred to know friends
                pass
            except BaseException as e:
                return_json |= {"Err": e.__str__()}

        data = request.GET.getlist('players')
        return_json |= request_get_all(data, 'Players', Player)
        return JsonResponse(return_json)

    def post(self, request, id: int = 0, ressource: str = "all"):
        data = request.data
        if not 'Id' in data:
            return JsonResponse({"Err": "no id provided"})
        if not 'Elo' in data:
            data['Elo'] = 500
        player = Player()
        player.unique_id = data['Id']
        player.elo = data['Elo']
        player.save()
        return JsonResponse({"Player": player.to_dict()})

    def delete(self, request, id: int = 0, ressource: str = "all"):
        data = request.data
        if not 'Id' in data:
            return JsonResponse({"Err": "no id provided"})
        try:
            player = Player.objects.get(unique_id=data['id'])
        except BaseException:
            return JsonResponse({"Err": "no player for the id"})
        return JsonResponse({"Player suppressed": True})

    def patch(self, request, id: int = 0, ressource: str = "all"):
        data = request.data
        if not 'Id' in data:
            return JsonResponse({"Err": "no id provided"})
        try:
            player = Player.objects.get(unique_id=data['id'])
        except BaseException:
            return JsonResponse({"Err": "no player for the id"})
        if not 'Elo' in data:
            return JsonResponse({"Err": "no elo provided"})
        player.elo = data['Elo']
        player.update()
        return JsonResponse({"Player updated": player.to_dict()})
