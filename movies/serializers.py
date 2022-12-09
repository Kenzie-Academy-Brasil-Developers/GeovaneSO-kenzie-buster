from rest_framework import serializers
from users.models import User
from users.serializers import UserSerializer
from movies.models import MovieRating, Movie
import ipdb


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(required=False)
    rating = serializers.ChoiceField(
        choices=MovieRating.choices,
        default=MovieRating.G
    )

    synopsis = serializers.CharField(required=False)

    added_by = UserSerializer()

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)