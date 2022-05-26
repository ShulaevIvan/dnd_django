from django.urls import path, include
from .views import CharacterListAllView, CharacterListItemView

urlpatterns = [
    path('character_list', CharacterListAllView.as_view(), name='characters'),
    path('character_list/<slug>', CharacterListItemView.as_view(), name='character'),
]