from films.models import Film, Actor, Producer, Genre
from games.models import Game
from rest_framework import serializers


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("name", "photo")


class ProducerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ("name", "photo")


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        exclude = ("slug",)

    producers = ProducerListSerializer(read_only=True, many=True)
    actors = ActorListSerializer(read_only=True, many=True)
    genre = GenreListSerializer(read_only=True, many=True)
