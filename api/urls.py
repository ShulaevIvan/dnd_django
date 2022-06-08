from rest_framework.routers import DefaultRouter

from .views import CharacterListViewSet

r = DefaultRouter()
r.register('character_list', CharacterListViewSet)

urlpatterns = r.urls