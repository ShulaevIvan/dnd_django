from email import charset
from tabnanny import verbose
from django.db import models
from users.models import User




class CharacterList(models.Model):

    name = models.CharField(max_length=200)
    player_name = models.CharField(max_length=200, blank=True)
    expirience = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    armor = models.IntegerField(blank=True, default=0)
    speed = models.IntegerField(blank=True, default=0,)
    iniciative = models.IntegerField(default=0, blank=True)
    max_health = models.IntegerField(default=10, blank=True)
    current_health = models.IntegerField(default=10, blank=True)
    multipler_health = models.IntegerField(default=6,blank=True)
    worldview = models.CharField(max_length=200, default='neutral')
    age = models.CharField(max_length=20, default=20, blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True, default='100 см')
    height = models.CharField(max_length=20, blank=True, null=True,default='100 см')
    appearance = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='list_owner')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:

        verbose_name = 'лист_персонажа'
        verbose_name_plural = 'листы_персонажей'

    def __str__(self):

        return self.name


class CharacterClass(models.Model):

    main = models.BooleanField(default=True)
    class_name = models.CharField(max_length=255)
    lvl = models.IntegerField(default=1)
    character_list = models.ForeignKey(CharacterList, on_delete=models.CASCADE, related_name='char_class')

    class Meta:

        verbose_name = 'класс_персонажа'
        verbose_name_plural = 'классы_персонажей'

    def __str__(self):

        return self.class_name


class CharacterCharacteristics(models.Model):

    strength = models.IntegerField(default=10, null=False)
    agility = models.IntegerField(default=10, null=False)
    stamina = models.IntegerField(default=10, null=False)
    intelligence = models.IntegerField(default=10, null=False)
    wisdom = models.IntegerField(default=10, null=False)
    charism = models.IntegerField(default=10, null=False)
    character_list = models.OneToOneField(CharacterList, on_delete=models.CASCADE, related_name='char_stats')

    class Meta:

        verbose_name = 'характеристики_персонажа'
        verbose_name_plural = 'характеристики_персонажей'

    def __str__(self):

        return str([self.strength, self.agility, self.stamina, self.wisdom, self.charism])


class CharacterAttributes(models.Model):

    athletics = models.IntegerField(default=0, null=True, blank=True)
    acrobatics = models.IntegerField(default=0, null=True, blank=True)
    sleight_of_hand = models.IntegerField(default=0, null=True, blank=True)
    stealth = models.IntegerField(default=0, null=True, blank=True)

    analysis = models.IntegerField(default=0, null=True, blank=True)
    history = models.IntegerField(default=0, null=True, blank=True)
    magic = models.IntegerField(default=0, null=True, blank=True)
    nature = models.IntegerField(default=0, null=True, blank=True)
    religion = models.IntegerField(default=0, null=True, blank=True)

    attentiveness = models.IntegerField(default=0, null=True, blank=True)
    survival = models.IntegerField(default=0, null=True, blank=True)
    medicine = models.IntegerField(default=0, null=True, blank=True)
    insight = models.IntegerField(default=0, null=True, blank=True)
    animal_care = models.IntegerField(default=0, null=True, blank=True)

    performance = models.IntegerField(default=0, null=True, blank=True)
    intimidation = models.IntegerField(default=0, null=True, blank=True)
    deception = models.IntegerField(default=0, null=True, blank=True)
    conviction = models.IntegerField(default=0, null=True, blank=True)

    character_list = models.OneToOneField(CharacterList, on_delete=models.CASCADE, related_name='char_atr')

    class Meta:

        verbose_name = 'навыки_персонажа'
        verbose_name_plural = 'навыки_персонажей'

    def __str__(self):

        return 'навыки персонажа'


class CharacterDeath(models.Model):

    failure = models.IntegerField(default=0, blank=True)
    success = models.IntegerField(default=0, blank=True)
    character_death_status = models.CharField(max_length=100, default='Alive', blank=True)
    character_list = models.ForeignKey(CharacterList, on_delete=models.CASCADE, related_name='char_death')

    class Meta:

        verbose_name = 'жизнь_и_смерть_персонажа'
        verbose_name_plural = 'жизнь_и_смерть_персонажаей'

    def __str__(self):

        return 'жизнь_и_смерть'


class CharacterSpells(models.Model):

    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    dmg_bonus = models.IntegerField(default=0, blank=True, null=True)
    dmg_type = models.CharField(max_length=150, blank=True, null=True)
    base_stat = models.CharField(max_length=100, blank=True, null=True)
    difficult = models.CharField(max_length=200, blank=True, null=True, default=1)
    lvl_spell = models.IntegerField(null=True, blank=True, default=1,)
    limit_per_day = models.IntegerField(null=True, blank=True, default=1)
    character_list = models.ForeignKey(CharacterList, on_delete=models.CASCADE, related_name='char_spells')

    class Meta:

        verbose_name = 'боевые_навыыкии_персонажа'
        verbose_name_plural = 'боевые_навыки_персонажей'
    def __str__(self):

        return self.name


class OtherSkills(models.Model):

    name = models.CharField(max_length=100)
    character_list = models.ForeignKey(CharacterList, on_delete=models.CASCADE, related_name='other_skills')

    class Meta:

        verbose_name = 'прочий_навык'
        verbose_name_plural = 'прочие_навыки'

    def __str__(self):

        return self.name


class PersonalityTraits(models.Model):

    name = models.CharField(max_length=200)
    ideal = models.TextField(max_length = 200, blank=True, null=True)
    bond = models.TextField(max_length = 200, blank=True, null=True)
    flaw = models.TextField(max_length = 200, blank=True, null=True)
    character_list = models.ForeignKey(CharacterList, on_delete=models.CASCADE, related_name='personality_traits')

    class Meta:

        verbose_name = 'персональные_особенности'
        verbose_name_plural = 'персональная_особенность'

    def __str__(self):

        return self.name


class CharacterItem(models.Model):

    name = models.CharField(max_length=255)
    rarity = models.CharField(max_length=255)
    character_list = models.ManyToManyField(CharacterList,  related_name='char_item', through='CharacterItemPosition')

    class Meta:

        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'

    def __str__(self):

        return self.name


class CharacterItemPosition(models.Model):

    character_list = models.ForeignKey(CharacterList, on_delete=models.CASCADE, related_name='item_positions')
    item = models.ForeignKey(CharacterItem, on_delete=models.CASCADE, related_name='item_positions')
    quantity = models.IntegerField(default=0)
    target_character_list = models.IntegerField(blank=True, null=True)


class CharacterRace(models.Model):

    name = models.CharField(max_length=200)
    race_bonuces = models.ManyToManyField(CharacterList, related_name='char_race', through='RaceCharacterBonuces')

    class Meta:

        verbose_name = 'Расса'
        verbose_name_plural = 'Рассы'

    def __str__(self):

        return self.name

class CharacterRaceBonuceSkill(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    dmg_bonus = models.IntegerField(default=0, blank=True, null=True)
    dmg_type = models.CharField(max_length=150, blank=True, null=True)

    class Meta:

        verbose_name = 'Рассовая способность'
        verbose_name_plural = 'Рассовые Способности'

    def __str__(self):

        return self.name

class CharacterRaceBonuceAtr(models.Model):

    strength_bonuce = models.IntegerField(default=0, null=True, blank=True)
    agility_bonuce = models.IntegerField(default=0, null=True, blank=True)
    stamina_bonuce = models.IntegerField(default=0, null=True, blank=True)
    intelligence_bonuce = models.IntegerField(default=0, null=True, blank=True)
    wisdom_bonuce = models.IntegerField(default=0, null=True, blank=True)
    charism_bonuce = models.IntegerField(default=0, null=True, blank=True)
    character_list = models.ForeignKey(CharacterList, on_delete=models.CASCADE, related_name='character_list')

    class Meta:

        verbose_name = 'Бонус характеристик'
        verbose_name_plural = 'Бонусы характеристик'

    def __str__(self):

        return 'Бонусы характеристик'


class RaceCharacterBonuces(models.Model):

    character_list = models.ForeignKey(CharacterList, on_delete=models.CASCADE, related_name='char_race_bonuce')
    race = models.ForeignKey(CharacterRace, on_delete=models.CASCADE, related_name='char_race_bonuce')
    bonuce_skills = models.ForeignKey(CharacterRaceBonuceSkill, on_delete=models.CASCADE, related_name='char_race_bonuce_skill')
    bonuce_atrs = models.ForeignKey(CharacterRaceBonuceAtr, on_delete=models.CASCADE, related_name='char_race_bonuce')

    class Meta:

        verbose_name = 'Расса и бонусы'
        verbose_name_plural = 'Рассовые бонусы'
    
    def __str__(self):

        return 'Рассовые бонусы'




    
    


