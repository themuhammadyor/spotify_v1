from rest_framework.pagination import LimitOffsetPagination

from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

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
    # def get_queryset(self, request):
    #     search = self.request.data
    #     data = Song.objects.filter(title=data)
    #     return Song.objects.all()

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'album__title', 'album__artist__name']
    pagination_class = LimitOffsetPagination
    # filter_backends = (DjangoFilterBackend)
    # filterset_fields = ['album__artist__name', 'album__title']

    # pagination_class = LimitOffsetPagination

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
