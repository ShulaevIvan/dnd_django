from unicodedata import name
from rest_framework.routers import DefaultRouter

from character_list.models import CharacterRace




from .views import CharacterClassViewSet, CharacterListViewSet, CharacterCharacteristcViewSet, CharacterItemViewset, \
CharacterItemPositionViewSet, GiveAwayItemPosition, CharacterLiveViewSet, CharacterSpellsViewSet, CharacterPersonalityTraits, \
RaceCharacterBonuces, CharacterRaceViewSet, CharacterRaceBonuceSkill, CharacterRaceBonuceAtr

r = DefaultRouter()
r.register('character_list', CharacterListViewSet)
r.register('character_characteristc', CharacterCharacteristcViewSet)
r.register('character_class', CharacterClassViewSet)
r.register('items', CharacterItemViewset)
r.register('character_items', CharacterItemPositionViewSet)
r.register('give_character_items', GiveAwayItemPosition)
r.register('character_status', CharacterLiveViewSet)
r.register('get_character_spells', CharacterSpellsViewSet)
r.register('personality_traits', CharacterPersonalityTraits)
r.register('character_race_skills', CharacterRaceBonuceSkill)
r.register('character_race', CharacterRaceViewSet)
r.register('character_race_atrs', CharacterRaceBonuceAtr)
r.register('character_race_bonuces', RaceCharacterBonuces)

urlpatterns = r.urls