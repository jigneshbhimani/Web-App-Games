from re import S
from app.models import Games, Genres, Publishers, Tags
from rest_framework import serializers
from django.contrib.auth.models import User

# --------------------User Serializer--------------------


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
# --------------------Register Serializer--------------------


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=10, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def validate(self, args):
        username = args.get('username', None)
        email = args.get('email', None)
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'email': ('Email already exists')})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'username': ('username already exists')})
        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
# --------------------Genres Serializer--------------------


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['id', 'type']
# --------------------Tags Serializer--------------------


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'tag']
# --------------------Publishers Serializer--------------------


class PublishersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishers
        fields = ['id', 'name']
# --------------------Games Serializer--------------------


class GamesSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=False)
    genres = GenresSerializer(many=True, read_only=False)
    publishers = PublishersSerializer(many=False, read_only=True)

    class Meta:
        model = Games
        fields = ['id', 'name', 'tags', 'genres', 'esrb', 'publishers',
                  'matacritics', 'description', 'best_of_all_time', 'release_date']
# --------------------Up Coming Games Serializer--------------------


class UpComingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['id', 'games', 'release_date']
