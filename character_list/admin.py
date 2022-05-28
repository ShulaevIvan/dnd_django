from django.contrib import admin

from .models import CharacterItem, CharacterList, CharacterCharacteristics, CharacterClass, \
    CharacterAtributes, CharacterSpells, OtherSkills, PersonalityTraits, CharacterItem, \
    CharacterItemPosition, CharacterDeath

class AdminCharacterClass(admin.TabularInline):
    
    model = CharacterClass
    extra = 0

class AdminCharacterCharacteristics(admin.TabularInline):

    model = CharacterCharacteristics
    extra = 0

class AdminCharacterAtributes(admin.TabularInline):

    model = CharacterAtributes
    extra = 0

class AdminCharacterSpells(admin.TabularInline):

    model = CharacterSpells
    extra = 0

class AdminOtherSkills(admin.TabularInline):

    model = OtherSkills
    extra = 0

class AdminPersonalityTraits(admin.TabularInline):

    model = PersonalityTraits
    extra = 0

class AdminCharacterItemPosition(admin.TabularInline):

    model = CharacterItemPosition
    exta = 0

class AdminCharacterDeath(admin.TabularInline):

    model = CharacterDeath
    extra = 0

@admin.register(CharacterItem)
class AdminCharacterItem(admin.ModelAdmin):

    list_display = ['id', 'name', 'rarity']

@admin.register(CharacterList)
class AdminCharacterList(admin.ModelAdmin):

    list_display = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        AdminCharacterClass,
        AdminCharacterCharacteristics,
        AdminCharacterAtributes,
        AdminCharacterSpells,
        AdminOtherSkills,
        AdminPersonalityTraits,
        AdminCharacterItemPosition,
        AdminCharacterDeath,
        
        ]



