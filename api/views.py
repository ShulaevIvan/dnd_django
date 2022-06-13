from rest_framework.viewsets  import ModelViewSet
from .serializers import CharacterClassSerializer, CharacterListSerializer, CharacterCharacteristicsSerializer
from character_list.models import CharacterList, CharacterCharacteristics, CharacterClass


class CharacterListViewSet(ModelViewSet):

    queryset = CharacterList.objects.all()
    serializer_class = CharacterListSerializer

class CharacterCharacteristcViewSet(ModelViewSet):

    queryset = CharacterCharacteristics.objects.all()
    serializer_class = CharacterCharacteristicsSerializer

class CharacterClassViewSet(ModelViewSet):

    queryset = CharacterClass.objects.all()
    serializer_class = CharacterClassSerializer