from django.shortcuts import render
from django.views import View
from .models import CharacterList


class CharacterListAllView(View):

    def get(self, request):

        data = CharacterList.objects.all()
        template_name = 'character_list.html'
        context = {
            'character': data
        }

        return render(request, template_name, context)



class CharacterListItemView(View):

    def get(self, request, slug):

        data = CharacterList.objects.filter(name=slug)
        template_name = 'character_list.html'
        context = {
            'character': data
        }

        return render(request, template_name, context)