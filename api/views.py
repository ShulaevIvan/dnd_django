from rest_framework.viewsets  import ModelViewSet
from .serializers import CharacterListSerializer, CharacterClassSerializer
from character_list.models import CharacterList, CharacterClass


class CharacterListViewSet(ModelViewSet):

    queryset = CharacterList.objects.all()
    serializer_class = CharacterListSerializer


    def get(self, request):
        print(request['data'])

class CharacterClassViewSet(ModelViewSet):

    queryset = CharacterClass.objects.all()
    serializer_class = CharacterClassSerializer