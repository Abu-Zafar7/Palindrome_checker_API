from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'games', GameViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('authenticate/',obtain_auth_token, name='api_token_auth')
]

