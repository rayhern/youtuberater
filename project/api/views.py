from django.shortcuts import render
from rest_framework import viewsets
from .models import Video, Rating
from .serializers import VideoSerializer, RatingSerializer, UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication


# Create your views here.
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @action(methods=['POST'], detail=True)
    def rate_video(self, request, pk=None):
        if 'stars' in request.data:
            video = Video.objects.get(id=pk)
            stars = request.data['stars']
            comments = request.data['comments']
            user = request.user
            try:
                rating = Rating.objects.get(user=user, video=video)
                rating.stars = stars
                rating.comments = comments
                rating.save()

                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating has been updated', 'response': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, video=video, stars=stars, comments=comments)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating has been created', 'response': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'please enter stars.'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        response = {'message': 'Rating cannot be deleted like this.'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
