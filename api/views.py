from urllib import request
from rest_framework.viewsets  import ModelViewSet
from .serializers import CharacterClassSerializer, CharacterListSerializer, CharacterCharacteristicsSerializer
from character_list.models import CharacterList, CharacterCharacteristics, CharacterClass


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