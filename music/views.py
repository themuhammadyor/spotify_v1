from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer


class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data={'message': 'Hi lazy developers'})

    def post(self, request):
        return Response(data={'post api': 'This is post request api'})


class ArtistAPIView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializers = ArtistSerializer(artists, many=True)
        return Response(data=serializers.data)


class AlbumAPIView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializers = AlbumSerializer(albums, many=True)
        return Response(data=serializers.data)


class AlbumAPIViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


# class SongAPIView(APIView):
#     def get(self, request):
#         songs = Song.objects.all()
#         serializers = SongSerializer(songs, many=True)
#         return Response(data=serializers.data)


class SongSetAPIView(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    # pagination_class = LimitOffsetPagination

    @action(default=True, method=["GET"])
    def view(self, request, *args, kwrgs):
        post = self.get_object()
        with atomic():
            post.viewing += 1
            post.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(default=False, method=["GET"])
    def top(self, request, *args, **kwargs):
        posts = self.get_queryset()
        posts = posts.order_by('-viewing')[:3]
        serializer = PostSerializer(songs, many=True)
        return Response(data=serializer.data)


# class SongDetailAPIView(APIView):
#     def get(self, request, id):
#         try:
#             song = Song.objects.get(id=id)
#             serializer = SongSerializer(song)
#             return Response(data=serializer.data)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def patch(self, request, id):
#         song = Song.objects.get(id=id)
#         serializer = SongSerializer(instance=song, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, id):
#         song = Song.objects.get(id=id)
#         serializer = SongSerializer(instance=song, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         song = Song.objects.get(id=id)
#         song.delete()
#
#         return Response(status=status.HTTP_204_NO_CONTENT)
