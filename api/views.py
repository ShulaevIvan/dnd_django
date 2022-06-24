from rest_framework.viewsets  import ModelViewSet
from .serializers import CharacterClassSerializer, CharacterListSerializer, CharacterCharacteristicsSerializer, \
CharacterItemSerializer, CharacterItemPositionSerializer, GiveAwayItemPositionSerializer, CharacterDeathSerializer, \
CharacterSpellsSerializer, PersonalityTraitsSerializer

from character_list.models import CharacterList, CharacterCharacteristics, CharacterClass, CharacterItem, CharacterItemPosition, \
CharacterDeath, CharacterSpells, PersonalityTraits


class CharacterListViewSet(ModelViewSet):

    queryset = CharacterList.objects.all()
    serializer_class = CharacterListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CharacterCharacteristcViewSet(ModelViewSet):

    queryset = CharacterCharacteristics.objects.all()
    serializer_class = CharacterCharacteristicsSerializer

class CharacterClassViewSet(ModelViewSet):

    queryset = CharacterClass.objects.all()
    serializer_class = CharacterClassSerializer

class CharacterItemViewset(ModelViewSet):

    queryset = CharacterItem.objects.all()
    serializer_class = CharacterItemSerializer

class CharacterItemPositionViewSet(ModelViewSet):

    queryset = CharacterItemPosition.objects.all()
    serializer_class = CharacterItemPositionSerializer

class GiveAwayItemPosition(ModelViewSet):

    queryset = CharacterItemPosition.objects.all()
    serializer_class = GiveAwayItemPositionSerializer

class CharacterLiveViewSet(ModelViewSet):

    queryset = CharacterDeath.objects.all()
    serializer_class = CharacterDeathSerializer

class CharacterSpellsViewSet(ModelViewSet):

    queryset = CharacterSpells.objects.all()
    serializer_class = CharacterSpellsSerializer

class CharacterPersonalityTraits(ModelViewSet):

    queryset = PersonalityTraits.objects.all()
    serializer_class = PersonalityTraitsSerializer

    
