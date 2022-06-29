from xml.etree.ElementInclude import include
from django.contrib import admin

from .models import CharacterItem, CharacterList, CharacterCharacteristics, CharacterClass, \
    CharacterAtributes, CharacterSpells, OtherSkills, PersonalityTraits, CharacterItem, \
    CharacterItemPosition, CharacterDeath, RaceCharacterBonuces, CharacterRace, CharacterRaceBonuceSkill, \
    CharacterRaceBonuceAtr

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
    extra = 0

class AdminCharacterDeath(admin.TabularInline):

    model = CharacterDeath
    extra = 0

class AdminRaceCharacterBonuces(admin.TabularInline):

    model = RaceCharacterBonuces
    extra = 0

class AdminCharacterRaceBonuceSkill(admin.TabularInline):

    model = CharacterRaceBonuceSkill
    extra = 0

@admin.register(CharacterRace)
class AdminCharacterRace(admin.ModelAdmin):

    list_display = ['id', 'name']

    def has_module_permission(self, request):
        return False

@admin.register(CharacterRaceBonuceSkill)
class AdminCharacterRaceBonuceSkill(admin.ModelAdmin):

    list_display =['id', 'description', 'dmg_bonus', 'dmg_type']

    def has_module_permission(self, request):
        return False

@admin.register(CharacterRaceBonuceAtr)
class AdminCharacterRaceBonuceAtr(admin.ModelAdmin):

    list_display =[
        'id', 
        'strength_bonuce',
        'agility_bonuce', 
        'stamina_bonuce',
        'intelligence_bonuce',
        'wisdom_bonuce',
        'charism_bonuce'
        ]

    def has_module_permission(self, request):
        return False

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
        AdminRaceCharacterBonuces
    ]







