from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action(detail=False, methods=['post'])
    def start_game(self, request):
        game = Game.objects.create(board="")
        return Response({'game_id': game.id})

    @action(detail=False, methods=['get'])
    def get_board(self, request):
        game_id = request.query_params.get('game_id')
        try:
            game = Game.objects.get(id=game_id)
            return Response({'board': game.board})
        except Game.DoesNotExist:
            return Response(status=404, data={'message': 'Game not found'})

    @action(detail=False, methods=['post'])
    def update_board(self, request):
        game_id = request.query_params.get('game_id')
        character = request.data.get('character', '').lower()
        if not character.isalpha() or len(character) != 1:
            return Response(status=400, data={'message': 'Invalid character'})

        try:
            game = Game.objects.get(id=game_id)
            game.board += character
            game.save()
            if len(game.board) == 6:
                game.is_palindrome = game.board == game.board[::-1]
                game.save()
                return Response({'message': 'Game over', 'is_palindrome': game.is_palindrome,'board': game.board})
            return Response({'message': 'Character added','board': game.board})
        except Game.DoesNotExist:
            return Response(status=404, data={'message': 'Game not found'})
