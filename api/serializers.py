from rest_framework import serializers
from  character_list.models import CharacterList, CharacterClass, CharacterCharacteristics


class CharacterClassSerializer(serializers.ModelSerializer):

    class Meta:

        model = CharacterClass
        fields = ['main', 'class_name', 'lvl']

class CharacterCharacteristicsSerializer(serializers.ModelSerializer):

    class Meta:

        model = CharacterCharacteristics
        fields = [
            'strength', 'agility', 'stamina', 
            'intelligence', 'wisdom', 'charism'
            ]
        
        

class CharacterListSerializer(serializers.ModelSerializer):
        
    char_class = CharacterClassSerializer(many=True)
    char_stats = CharacterCharacteristicsSerializer(many=False)

    class Meta:

        model = CharacterList
        fields = [
            'id', 'name', 'player_name', 'expirience', 
            'armor', 'speed', 'iniciative',
            'max_health', 'current_health',
            'multipler_health', 'char_class', 'char_stats',
        ]
        read_only_fields = ('char_class', 'char_stats',)
        # depth = 1











