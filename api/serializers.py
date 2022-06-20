from rest_framework import serializers
from rest_framework.validators import ValidationError
from users.models import User
from  character_list.models import CharacterList, CharacterClass, CharacterCharacteristics, CharacterItem, CharacterItemPosition


class CharacterClassSerializer(serializers.ModelSerializer):

    class Meta:

        model = CharacterClass
        fields = ['id', 'main', 'class_name', 'lvl', 'character_list']


    def create(self, validated_data):
        class_added = validated_data.pop('class_name')
        char_list = validated_data.pop('character_list')
        char_class = CharacterClass.objects.all().filter(character_list=char_list.id)

        for i in char_class:

            if str(class_added) == str(i):
                raise ValidationError('Класс существует')

        char_class = CharacterClass.objects.create(class_name= class_added, character_list = char_list, **validated_data)
        
        return char_class
            

class CharacterCharacteristicsSerializer(serializers.ModelSerializer):

    class Meta:

        model = CharacterCharacteristics
        fields = [
            'id', 'strength', 'agility', 'stamina', 
            'intelligence', 'wisdom', 'charism', 'character_list',
            ]

    def create(self, validated_data):

        character_list = validated_data.pop('character_list')
        char_obj = CharacterCharacteristics.objects.create(character_list=character_list, **validated_data)

        return char_obj

class CharacterListSerializer(serializers.ModelSerializer):

    char_class = CharacterClassSerializer(many=True, read_only=True)
    char_stats = CharacterCharacteristicsSerializer(many=False, read_only=True)

    class Meta:

        model = CharacterList
        fields = [
            'id', 'owner', 'name', 'player_name', 'expirience', 
            'armor', 'speed', 'iniciative',
            'max_health', 'current_health',
            'multipler_health', 'char_class', 'char_stats'
        ]

        read_only_fields = ['owner']

    def create(self, validated_data):

        owner = validated_data.pop('owner')
        slug = validated_data.pop('name')
        characters = User.objects.all().filter(email=owner)

        for i in characters:
            
            user_id = i.id
            char_list = CharacterList.objects.create(owner_id = user_id, name = slug, slug = slug,  **validated_data)
            
        return char_list


class CharacterItemSerializer(serializers.ModelSerializer):


    class Meta:

        model = CharacterItem
        fields = ['id', 'name', 'rarity']
        read_only_fields = ['id']
    
    def create(self, validated_data):

        name = validated_data['name']

        if CharacterItem.objects.all().filter(name=name).exists():

            raise ValidationError('Предмет существует!')

        return super().create(validated_data)

class CharacterItemPositionSerializer(serializers.ModelSerializer):

    item = CharacterItemSerializer

    class Meta:

        model = CharacterItemPosition
        fields = ['id', 'character_list', 'item', 'quantity']
        exclude_fields = ['target_character_list']

class GiveAwayItemPositionSerializer(serializers.ModelSerializer):

    class Meta:

        model = CharacterItemPosition
        fields = ['id', 'character_list', 'item', 'target_character_list']

    def create(self, validated_data):

        give_item = validated_data['item']
        target_character_id = validated_data['target_character_list']
        current_character = validated_data['character_list']
        current_character_items = CharacterItemPosition.objects.all().filter(character_list = current_character)
        character_obj = CharacterItemPosition.objects.all().filter(character_list_id=target_character_id).filter(item_id = give_item.id)


        for i in current_character_items:
            print(i.item)

            if i.item == give_item:
                qnt_obj = CharacterItemPosition.objects.all().filter(character_list = current_character, item=i.item)
                for qnt in qnt_obj:
                    if qnt.quantity >= 1:
                        qnt.quantity -= 1
                        qnt.save()
                        target_character_positions = qnt
                    else:
                        current_character_items = CharacterItemPosition.objects.all().filter(character_list = current_character, item=i.item).delete()
                        raise ValidationError('Предметы закончились')
                        
                if character_obj.exists():
                    for qnt in character_obj:
                        qnt.quantity += 1
                        qnt.save()
                        target_character_positions = qnt 
                else:
                    target_character_positions = CharacterItemPosition.objects.create(character_list_id=target_character_id, item_id = give_item.id, quantity = +1)

            return target_character_positions




        
        





        

        




