from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from .models import CharacterList


class CharacterListAllView(View):

    def get(self, request):
        data = CharacterList.objects.all()
        template_name = 'character_list_all.html'
        context = {
            'character': data
        }

        return render(request, template_name, context)


class CharacterListItemView(PermissionRequiredMixin, View):

    permission_required = 'character_list.view_post'

    def get(self, request, slug):

        data = CharacterList.objects.all().filter(name=slug)
        template_name = 'character_list.html'
        context = {
            'character': data
        }

        return render(request, template_name, context)