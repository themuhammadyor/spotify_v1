from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LandingPageAPIView, ArtistAPIView, AlbumAPIViewSet, SongSetAPIView
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('albums', viewset=AlbumAPIViewSet)
router.register('songs', viewset=SongSetAPIView)

urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name='landing'),
    path('artists/', ArtistAPIView.as_view(), name='artists'),
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]
