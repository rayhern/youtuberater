from rest_framework import serializers
from .models import Video, Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'rating_average', 'url', 'category', 'subcategory', 'author', 'comments_list')
        extra_kwargs = {'url': {'required': True}}

    def create(self, validated_data):
        url = validated_data['url']
        video_id = url[url.index('?v=') + 3:]
        if '&' in video_id:
            video_id = video_id[:video_id.index('&')]
        validated_data['url'] = 'https://www.youtube.com/embed/%s' % video_id
        return Video.objects.create(**validated_data)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'video', 'comments')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
