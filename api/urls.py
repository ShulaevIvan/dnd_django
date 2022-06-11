from rest_framework.routers import DefaultRouter

from .views import CharacterListViewSet, CharacterCharacteristcViewSet

r = DefaultRouter()
r.register('character_list', CharacterListViewSet)
r.register('character_characteristc', CharacterCharacteristcViewSet)

urlpatterns = r.urls