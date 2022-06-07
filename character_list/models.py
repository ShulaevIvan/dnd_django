from django.db import models
from users.models import User


class CharacterList(models.Model):

    name = models.CharField(max_length=200)
    player_name = models.CharField(max_length=200, blank=True)
    expirience = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    armor = models.IntegerField(default=0, blank=True)
    speed = models.IntegerField(default=0, blank=True)
    iniciative = models.IntegerField(default=0, blank=True)
    max_health = models.IntegerField(default=10, blank=True)
    current_health = models.IntegerField(default=10, blank=True)
    multipler_health = models.IntegerField(default=6,blank=True)
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


class CharacterAtributes(models.Model):

    acrobatics = models.IntegerField(default=0, null=True, blank=True)
    athletics = models.IntegerField(default=0, null=True, blank=True)
    training = models.IntegerField(default=0, null=True, blank=True)
    deception = models.IntegerField(default=0, null=True, blank=True)
    history = models.IntegerField(default=0, null=True, blank=True)
    attention = models.IntegerField(default=0, null=True, blank=True)
    intimidation = models.IntegerField(default=0, null=True, blank=True)
    investigation = models.IntegerField(default=0, null=True, blank=True)
    medicine = models.IntegerField(default=0, null=True, blank=True)
    nature = models.IntegerField(default=0, null=True, blank=True)
    insight = models.IntegerField(default=0, null=True, blank=True)
    execution = models.IntegerField(default=0, null=True, blank=True)
    persuasion = models.IntegerField(default=0, null=True, blank=True)
    Religion = models.IntegerField(default=0, null=True, blank=True)
    sleight_of_hand = models.IntegerField(default=0, null=True, blank=True)
    stealth = models.IntegerField(default=0, null=True, blank=True)
    survival = models.IntegerField(default=0, null=True, blank=True)
    character_list = models.OneToOneField(CharacterList, on_delete=models.CASCADE, related_name='char_atr')

    class Meta:

        verbose_name = 'навыки_персонажа'
        verbose_name_plural = 'навыки_персонажей'

    def __str__(self):

        return 'навыки персонажа'


class CharacterDeath(models.Model):

    failure = models.IntegerField(default=0, blank=True, null=True)
    success = models.IntegerField(default=0, blank=True, null=True)
    character_list = models.ForeignKey(CharacterList, on_delete=models.CASCADE, related_name='char_death')

    class Meta:

        verbose_name = 'жизнь_и_смерть_персонажа'
        verbose_name_plural = 'жизнь_и_смерть_персонажаей'

    def __str__(self):

        return 'жизнь_и_смерть'


class CharacterSpells(models.Model):

    name = models.CharField(max_length=200, blank=True, null=True)
    dmg_bonus = models.IntegerField(default=0, blank=True, null=True)
    dmg_type = models.CharField(max_length=150, blank=True, null=True)
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
    character_list = models.ForeignKey(CharacterList, on_delete=models.CASCADE, related_name='personality_traits')

    class Meta:

        verbose_name = 'персональный_навык'
        verbose_name_plural = 'персональныые_навык'

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
