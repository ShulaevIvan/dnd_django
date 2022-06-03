from rest_framework import serializers
from  character_list.models import CharacterList, CharacterClass, CharacterCharacteristics



class CharacterListSerializer(serializers.ModelSerializer):

    char_class = serializers.StringRelatedField(
        many=True,
        read_only=True,
        )
        
    class Meta:

        model = CharacterList
        fields = [
            'id', 'name', 'player_name', 'expirience', 
            'armor', 'speed', 'iniciative',
            'max_health', 'current_health',
            'multipler_health', 'char_class','char_stats'
        ]



class CharacterClassSerializer(serializers.ModelSerializer):

    class Meta:

        model = CharacterClass
        fields = ['id', 'class_name', 'character_list', 'main']
        read_only_fields = ['character_list', 'char_class']






