from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework import status

from django.contrib.sessions.models import Session
from users.models import User
from  character_list.models import CharacterList, CharacterClass, CharacterCharacteristics, CharacterItem, CharacterItemPosition, \
CharacterDeath, CharacterSpells, PersonalityTraits, CharacterRaceBonuceSkill, CharacterRace, RaceCharacterBonuces , \
CharacterRaceBonuceAtr, OtherSkills, CharacterAttributes

from users.models import UserTokens



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
            'multipler_health', 'char_class', 'char_stats',
            'worldview','age', 'weight', 'height', 'appearance',
            'history' 
        ]

        read_only_fields = ['owner']

    def create(self, validated_data):

        owner = validated_data.pop('user')
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

class CharacterDeathSerializer(serializers.ModelSerializer):

    class Meta:

        model = CharacterDeath
        fields = ['id', 'success', 'failure', 'character_list', 'character_death_status']

    def create(self, validated_data):

        failure = validated_data.get('failure')
        success = validated_data.get('success')
        character_death_status = validated_data.get('character_death_status')

        char_death_check = CharacterDeath.objects.all().filter(character_list = validated_data['character_list']).exists()
        char_death_obj = CharacterDeath.objects.all().filter(character_list = validated_data['character_list'])


        if char_death_check:
            
            for i in char_death_obj:
                char_obj = i

                if success:
                    i.success += success
                    i.save()

                elif failure and i.failure < 3:
                    i.failure += failure
                    i.save()

                elif i.failure >= 3 and character_death_status != 'Alive':
                    i.character_death_status = 'Death'
                    i.save()
                    
                    raise ValidationError("Персонаж Мертв")

                if character_death_status == 'Alive':
                    i.character_death_status = 'Alive'
                    i.success = 0
                    i.failure = 0
                    i.save()
        else:
            char_obj = CharacterDeath.objects.create(**validated_data)

        return char_obj

class CharacterSpellsSerializer(serializers.ModelSerializer):

    class Meta:

        model = CharacterSpells
        fields = ['id', 
                  'name', 
                  'dmg_bonus', 
                  'dmg_type',  
                  'base_stat', 
                  'difficult',
                  'lvl_spell',
                  'limit_per_day',
                  'character_list'
                ]

class PersonalityTraitsSerializer(serializers.ModelSerializer):

    class Meta:

        model = PersonalityTraits
        fields = ['id', 'name','ideal', 'bond', 'flaw', 'character_list']

class CharacterRaceBonuceSkillSerializer(serializers.ModelSerializer):

    class Meta:

        model = CharacterRaceBonuceSkill
        fields = ['id', 'name', 'description', 'dmg_bonus', 'dmg_type']

class CharacterRaceSerializer(serializers.ModelSerializer):

    class Meta:

        model = CharacterRace
        fields = ['id','name']

class CharacterRaceBonuceAtrSerializer(serializers.ModelSerializer):

    class Meta:

        model = CharacterRaceBonuceAtr
        fields = [  'id',
                    'character_list',
                    'strength_bonuce', 
                    'agility_bonuce', 
                    'stamina_bonuce', 
                    'intelligence_bonuce',
                    'wisdom_bonuce',
                    'charism_bonuce'
                ]

class RaceCharacterBonucesSerialier(serializers.ModelSerializer):

    class Meta:

        model = RaceCharacterBonuces
        fields = ['id','character_list', 'race', 'bonuce_skills', 'bonuce_atrs']

    def create(self, validated_data):

        character_id = validated_data.pop('character_list')

        for obj in validated_data:
            race_b, create_tuple = RaceCharacterBonuces.objects.update_or_create(character_list = character_id, **validated_data )

        return race_b

class OtherSkillsSerializer(serializers.ModelSerializer):

    class Meta:

        model = OtherSkills
        fields = ['name', 'character_list']

class CharacterAttributesSerializer(serializers.ModelSerializer):



    class Meta:

        model = CharacterAttributes
        fields = [
            'athletics','acrobatics','sleight_of_hand',
            'stealth','analysis','history','magic',
            'nature','religion','attentiveness',
            'survival','medicine','insight','animal_care',
            'performance','intimidation','deception','conviction',
            'character_list'
        ]
        related_fields = ['character_list']
        salary = serializers.IntegerField(source='character_list.id')

    def update(self, instance, validated_data):

        character_list = validated_data.pop('character_list')
        character_atrs = super().update(instance, validated_data)
        
        character, create_tuple = CharacterAttributes.objects.update_or_create(character_list = character_list, **validated_data)
        character.save()

        return character_atrs

class UserTokensSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserTokens
        fields = ['user', 'token']
        read_only_fields = ['token']

    def create(self, validated_data):

        user = UserTokens.objects.all()

        session_key = validated_data.pop('user')
        session = Session.objects.get(session_key=session_key)
        session_data = session.get_decoded()
        uid = session_data.get('_auth_user_id')
        user = User.objects.get(id=uid)
        token = UserTokens.objects.all().filter(user=user)

        exeption = serializers.ValidationError(token[0].token)
        exeption.status_code = 200

        raise exeption
        
      




        
        





        

        




