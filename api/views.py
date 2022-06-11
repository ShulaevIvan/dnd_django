from rest_framework.viewsets  import ModelViewSet
from .serializers import CharacterListSerializer, CharacterCharacteristicsSerializer
from character_list.models import CharacterList, CharacterCharacteristics


class CharacterListViewSet(ModelViewSet):

    queryset = CharacterList.objects.all()
    serializer_class = CharacterListSerializer

class CharacterCharacteristcViewSet(ModelViewSet):

    queryset = CharacterCharacteristics.objects.all()
    serializer_class = CharacterCharacteristicsSerializer