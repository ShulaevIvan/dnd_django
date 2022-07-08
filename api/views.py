from urllib import request
from rest_framework.viewsets  import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperAdmin

import random

from .serializers import CharacterClassSerializer, CharacterListSerializer, CharacterCharacteristicsSerializer, \
CharacterItemSerializer, CharacterItemPositionSerializer, GiveAwayItemPositionSerializer, CharacterDeathSerializer, \
CharacterSpellsSerializer, OtherSkillsSerializer, PersonalityTraitsSerializer, RaceCharacterBonucesSerialier, CharacterRaceBonuceSkillSerializer, \
CharacterRaceSerializer, CharacterRaceBonuceAtrSerializer, CharacterAttributesSerializer, UserTokensSerializer

from character_list.models import CharacterList, CharacterCharacteristics, CharacterClass, CharacterItem, CharacterItemPosition, \
CharacterDeath, CharacterSpells, OtherSkills, PersonalityTraits, CharacterRaceBonuceSkill, CharacterRace, RaceCharacterBonuces, \
CharacterRaceBonuceAtr, CharacterAttributes

from users.models import UserTokens

class RollD4View(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        if 'dice' not in request.data:
            return Response(['dice field is required.'], status=400)
        elif 'count' not in request.data:
            return Response(['count field is required.'], status=400)

        dice = request.data.get('dice')
        count = request.data.get('count')
        modif = request.data.get('modif')
        roll_obj = dict()

        if not modif:
            modif = 0
     
        for roll in range(1, count+1):
            value = random.randint(1, dice)
            if value == dice:
                roll_obj[f'cast_{roll}_critical_success'] = value
            elif value == 1:
                roll_obj[f'cast_{roll}_critical_failure'] = value


            roll_obj[f'cast_{roll}'] = {'value': value, 'modif': modif, 'sum_value': value + modif}

        return Response(roll_obj)


class CharacterListViewSet(ModelViewSet):

    queryset = CharacterList.objects.all()
    serializer_class = CharacterListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'player_name']
    search_fields = ['name', 'player_name']

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

class CharacterRaceBonuceSkill(ModelViewSet):

    queryset = CharacterRaceBonuceSkill.objects.all()
    serializer_class = CharacterRaceBonuceSkillSerializer

class CharacterRaceViewSet(ModelViewSet):

    queryset = CharacterRace.objects.all()
    serializer_class = CharacterRaceSerializer

class CharacterRaceBonuceAtr(ModelViewSet):

    queryset = CharacterRaceBonuceAtr.objects.all()
    serializer_class = CharacterRaceBonuceAtrSerializer

class RaceCharacterBonuces(ModelViewSet):

    queryset = RaceCharacterBonuces.objects.all()
    serializer_class = RaceCharacterBonucesSerialier

class CharacterOtherSkill(ModelViewSet):

    queryset = OtherSkills.objects.all()
    serializer_class = OtherSkillsSerializer

class CharacterAttributesView(ModelViewSet):

    queryset = CharacterAttributes.objects.all()
    serializer_class = CharacterAttributesSerializer

class UserTokenView(ModelViewSet):

    queryset = UserTokens.objects.all()
    serializer_class = UserTokensSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['user']
    search_fields = ['user']

    def get_permissions(self):

        if self.action in ["list", "create", "update", "partial_update", 'destroy']:
            return [IsSuperAdmin(), IsAuthenticated()]
        return []

