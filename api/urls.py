from rest_framework.routers import DefaultRouter

from .views import CharacterClassViewSet, CharacterListViewSet, CharacterCharacteristcViewSet

r = DefaultRouter()
r.register('character_list', CharacterListViewSet)
r.register('character_characteristc', CharacterCharacteristcViewSet)
r.register('character_class', CharacterClassViewSet)

urlpatterns = r.urls