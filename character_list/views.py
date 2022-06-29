from math import modf
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.db.models import Sum
from .models import CharacterList, CharacterCharacteristics, CharacterClass, CharacterAtributes, \
CharacterDeath, CharacterItemPosition, CharacterRaceBonuceAtr, CharacterSpells, OtherSkills, PersonalityTraits, RaceCharacterBonuces


class CharacterListAllView(View):

    permission_required = 'character_list.view_post'

    def get(self, request):

        data = CharacterList.objects.all().filter(owner=request.user)
        template_name = 'character_list_all.html'
        context = {
            'character': data
        }

        return render(request, template_name, context)


class CharacterListItemView(View):

    permission_required = 'character_list.view_post'

    def get_modifer(self, stat_obj, param, race_m = None):

        modif_default = -5

        if race_m:
            modif_default += race_m

        for item in stat_obj.values():

            for i in range(1, 31):
                if i % 2 == 0:
                    modif_default += 1

                if item[param] == i:  
                    return modif_default

                elif item[param] and item[param] > 30:

                    modif_default = 10
                    return modif_default

    def get_max_health(self, char_lvl, char_multipler_helth, modif_stamina):

        tmp_lvl = 0
        for lvl in char_lvl:
            tmp_lvl += lvl

        return tmp_lvl * char_multipler_helth[0] + modif_stamina


    def get_atr_modifer(self, atr_obj, stats_modif):

        atr_set = {
            'acrobatics': 'agility',
            'athletics' : 'strength',
            'training' : 'wisdom',
            'deception': 'charism',
            'attention' : 'wisdom',
            'history ': 'intelligence',
            'investigation': 'intelligence',
            'nature' : 'intelligence',
            'intimidation' : 'charism',
            'medicine' : 'wisdom',
            'religion ' : 'intelligence',
            'insight' : 'wisdom',
            'execution' : 'charism',
            'persuasion' : 'wisdom',
            'sleight_of_hand' : 'agility',
            'stealth' : 'agility',
            'survival' : 'wisdom'
        }

        clear_atr = {}

        for obj in atr_obj.values():
            for k, v in obj.items():
                if k in atr_set:
                    clear_atr[k] = obj[k] + stats_modif[atr_set[k]]
        return clear_atr

    def get_race(self, character):

            atr_bonuce = CharacterRaceBonuceAtr.objects.all().filter(character_list = character[0].id)
            clear_atr_bonuces = dict()
            for atr_obj in atr_bonuce.values():
                for v, k in enumerate(atr_obj):
                    if atr_obj[k] > 0 and k != 'id' and k != 'character_list_id':
                        clear_atr_bonuces[k] = atr_obj[k]
                    elif atr_obj[k] == 0 and k != 'id' and k != 'character_list_id':
                        clear_atr_bonuces[k] = atr_obj[k]
            for v, k in enumerate(list(clear_atr_bonuces)):

                if clear_atr_bonuces[k] % 2 == 0:
                    clear_atr_bonuces[f'modif_'+k] = round(clear_atr_bonuces[k] / 2)
                else:
                    clear_atr_bonuces[f'modif_'+k] = round((clear_atr_bonuces[k] -1) / 2)

            return clear_atr_bonuces
            
    def get(self, request, slug):
        
        character = CharacterList.objects.all().filter(name=slug).filter(owner=request.user)
        char_stats = CharacterCharacteristics.objects.all().filter(character_list = character[0].id)
        char_class = CharacterClass.objects.all().filter(character_list = character[0].id)
        char_death = CharacterDeath.objects.all().filter(character_list = character[0].id)
        char_atributes = CharacterAtributes.objects.all().filter(character_list = character[0].id)
        char_items = CharacterItemPosition.objects.all().filter(character_list = character[0].id)
        char_spells = CharacterSpells.objects.all().filter(character_list = character[0].id)
        char_other_skills = OtherSkills.objects.all().filter(character_list = character[0].id)
        char_personality_traits = PersonalityTraits.objects.all().filter(character_list = character[0].id)
        race_bonuces = RaceCharacterBonuces.objects.all().filter(character_list = character[0].id)
        clear_stats = {}
        stats_modif = {}


        if CharacterRaceBonuceAtr.objects.all().filter(character_list_id = character[0].id).exists():
            clear_race_bonuces = self.get_race(character)
        else:
            clear_race_bonuces = {
                'strength_bonuce': 0, 
                'agility_bonuce': 0, 
                'stamina_bonuce': 0, 
                'intelligence_bonuce': 0, 
                'wisdom_bonuce': 0, 
                'charism_bonuce': 0, 
                'modif_strength_bonuce': 0, 
                'modif_agility_bonuce': 0, 
                'modif_stamina_bonuce': 0, 
                'modif_intelligence_bonuce': 0, 
                'modif_wisdom_bonuce': 0, 
                'modif_charism_bonuce': 0
            }
        
        for i in char_stats.values():
            if i == i['id'] or i == i['character_list_id']:
                continue
            else:
                clear_stats['strength'] = i['strength']
                clear_stats['agility'] = i['agility']
                clear_stats['intelligence'] = i['intelligence']
                clear_stats['stamina'] = i['stamina']
                clear_stats['wisdom'] = i['wisdom']
                clear_stats['charism'] = i['charism'] 

        for k in clear_stats.keys():

            race_m = 0

            if f'modif_{k}_bonuce' in clear_race_bonuces:
                race_m = clear_race_bonuces[f'modif_{k}_bonuce']
                del clear_race_bonuces[f'modif_{k}_bonuce']

            stats_modif[k] = self.get_modifer(char_stats, k, race_m)
            
        char_atrs = self.get_atr_modifer(char_atributes, stats_modif)

        char_lvl = CharacterClass.objects.filter(character_list = character[0].id).values_list('lvl', flat=True)
        char_multipler_helth = CharacterList.objects.filter(id = character[0].id).values_list('multipler_health', flat=True)
        max_health = self.get_max_health(char_lvl, char_multipler_helth, stats_modif['stamina'])

        template_name = 'character_list.html'
        context = {
            'character': character,
            'char_stats': char_stats,
            'char_max_health': max_health,
            'char_modif': stats_modif,
            'char_atrs': char_atrs,
            'char_death': char_death,
            'char_class': char_class,
            'char_items': char_items,
            'char_spells': char_spells,
            'char_person_traits': char_personality_traits,
            'char_other_skills': char_other_skills,
            'race_bonuces': race_bonuces,
            'race_bonuces_int': clear_race_bonuces
        }

        return render(request, template_name, context)
