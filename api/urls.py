from rest_framework.routers import DefaultRouter

from character_list.models import CharacterClass
from .views import CharacterListViewSet, CharacterClassViewSet

r = DefaultRouter()
r.register('character_list', CharacterListViewSet)
r.register('character_class', CharacterClassViewSet)

urlpatterns = r.urls