from rest_framework.routers import DefaultRouter

from .views import CharacterClassViewSet, CharacterListViewSet, CharacterCharacteristcViewSet, CharacterItemViewset, \
CharacterItemPositionViewSet, GiveAwayItemPosition

r = DefaultRouter()
r.register('character_list', CharacterListViewSet)
r.register('character_characteristc', CharacterCharacteristcViewSet)
r.register('character_class', CharacterClassViewSet)
r.register('get_items', CharacterItemViewset)
r.register('get_character_items', CharacterItemPositionViewSet)
r.register('give_character_items', GiveAwayItemPosition)

urlpatterns = r.urls