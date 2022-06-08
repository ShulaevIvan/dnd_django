from rest_framework.viewsets  import ModelViewSet
from .serializers import CharacterListSerializer
from character_list.models import CharacterList


class CharacterListViewSet(ModelViewSet):

    queryset = CharacterList.objects.all()
    serializer_class = CharacterListSerializer