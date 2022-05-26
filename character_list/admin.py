from django.contrib import admin

from .models import CharacterList

@admin.register(CharacterList)
class AdminCharacterList(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}
