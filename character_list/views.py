from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from .models import CharacterList, CharacterCharacteristics, CharacterClass, CharacterAtributes


class CharacterListAllView(PermissionRequiredMixin, View):

    permission_required = 'character_list.view_post'

    def get(self, request):

        data = CharacterList.objects.all().filter(owner=request.user)
        template_name = 'character_list_all.html'
        context = {
            'character': data
        }

        return render(request, template_name, context)


class CharacterListItemView(PermissionRequiredMixin, View):

    permission_required = 'character_list.view_post'

    def get_modifer(self, stat_obj, param):

        modif_default = -5

        for item in stat_obj.values():
            print(item[param])
            for i in range(1, 31):
                if i % 2 == 0:
                    modif_default += 1

                if item[param] == i:
                    
                    return modif_default
                elif item[param] and item[param] > 30:
                    modif_default = 10

                    return modif_default


    def get_atr_modifer(self, atr_obj, stats_modif):

        atr_set = {
            'acrobatics': 'agility',
            'athletics' : 'strength',
            'training' : 'wisdom',
            'deception': 'charism',
            'attention' : 'wisdom',
            'intimidation' : 'charism',
            'medicine' : 'wisdom',
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
                print(k)
                if k in atr_set:
                    clear_atr[k] = obj[k] + stats_modif[atr_set[k]]
        print(clear_atr)
        return clear_atr



    def get(self, request, slug):

        character = CharacterList.objects.all().filter(name=slug).filter(owner=request.user)
        char_stats = CharacterCharacteristics.objects.all().filter(charcter_list = character[0].id)
        char_class = CharacterClass.objects.all().filter(character_list = character[0].id)
        char_atributes = CharacterAtributes.objects.all().filter(charcter_list = character[0].id)
        clear_stats = {}
        stats_modif = {}

        for i in char_stats.values():
            if i == i['id']or i == i['charcter_list_id']:
                continue
            else:
                clear_stats['strength'] = i['strength']
                clear_stats['agility'] = i['agility']
                clear_stats['stamina'] = i['stamina']
                clear_stats['wisdom'] = i['wisdom']
                clear_stats['charism'] = i['charism']

        for k in clear_stats.keys():
            stats_modif[k] = self.get_modifer(char_stats, k)

        char_atrs = self.get_atr_modifer(char_atributes, stats_modif)
        template_name = 'character_list.html'

        context = {
            'character': character,
            'char_stats': char_stats,
            'char_modif': stats_modif,
            'char_atrs': char_atrs,
            'char_class': char_class
        }

        return render(request, template_name, context)
