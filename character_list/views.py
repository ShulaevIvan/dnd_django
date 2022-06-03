from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from .models import CharacterList


class CharacterListAllView(PermissionRequiredMixin, View):

    permission_required = 'character_list.view_post'

    def get(self, request):
        print(request.user)
        data = CharacterList.objects.all().filter(owner=request.user)
        template_name = 'character_list_all.html'
        context = {
            'character': data
        }

        return render(request, template_name, context)


class CharacterListItemView(PermissionRequiredMixin, View):

    permission_required = 'character_list.view_post'

    def get(self, request, slug):

        data = CharacterList.objects.all().filter(name=slug).filter(owner=request.user)
        template_name = 'character_list.html'
        context = {
            'character': data
        }

        return render(request, template_name, context)
