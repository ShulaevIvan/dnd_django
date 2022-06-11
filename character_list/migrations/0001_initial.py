# Generated by Django 4.0.4 on 2022-06-10 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rarity', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'предмет',
                'verbose_name_plural': 'предметы',
            },
        ),
        migrations.CreateModel(
            name='CharacterList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('player_name', models.CharField(blank=True, max_length=200)),
                ('expirience', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('armor', models.IntegerField(blank=True, default=0)),
                ('speed', models.IntegerField(blank=True, default=0)),
                ('iniciative', models.IntegerField(blank=True, default=0)),
                ('max_health', models.IntegerField(blank=True, default=10)),
                ('current_health', models.IntegerField(blank=True, default=10)),
                ('multipler_health', models.IntegerField(blank=True, default=6)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'лист_персонажа',
                'verbose_name_plural': 'листы_персонажей',
            },
        ),
        migrations.CreateModel(
            name='PersonalityTraits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('character_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personality_traits', to='character_list.characterlist')),
            ],
            options={
                'verbose_name': 'персональный_навык',
                'verbose_name_plural': 'персональныые_навык',
            },
        ),
        migrations.CreateModel(
            name='OtherSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('character_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_skills', to='character_list.characterlist')),
            ],
            options={
                'verbose_name': 'прочий_навык',
                'verbose_name_plural': 'прочие_навыки',
            },
        ),
        migrations.CreateModel(
            name='CharacterSpells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('dmg_bonus', models.IntegerField(blank=True, default=0, null=True)),
                ('dmg_type', models.CharField(blank=True, max_length=150, null=True)),
                ('character_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='char_spells', to='character_list.characterlist')),
            ],
            options={
                'verbose_name': 'боевые_навыыкии_персонажа',
                'verbose_name_plural': 'боевые_навыки_персонажей',
            },
        ),
        migrations.CreateModel(
            name='CharacterItemPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('character_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_positions', to='character_list.characterlist')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_positions', to='character_list.characteritem')),
            ],
        ),
        migrations.AddField(
            model_name='characteritem',
            name='character_list',
            field=models.ManyToManyField(related_name='char_item', through='character_list.CharacterItemPosition', to='character_list.characterlist'),
        ),
        migrations.CreateModel(
            name='CharacterDeath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failure', models.IntegerField(blank=True, default=0, null=True)),
                ('success', models.IntegerField(blank=True, default=0, null=True)),
                ('character_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='char_death', to='character_list.characterlist')),
            ],
            options={
                'verbose_name': 'жизнь_и_смерть_персонажа',
                'verbose_name_plural': 'жизнь_и_смерть_персонажаей',
            },
        ),
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.BooleanField(default=True)),
                ('class_name', models.CharField(max_length=255)),
                ('lvl', models.IntegerField(default=1)),
                ('character_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='char_class', to='character_list.characterlist')),
            ],
            options={
                'verbose_name': 'класс_персонажа',
                'verbose_name_plural': 'классы_персонажей',
            },
        ),
        migrations.CreateModel(
            name='CharacterCharacteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField(default=10)),
                ('agility', models.IntegerField(default=10)),
                ('stamina', models.IntegerField(default=10)),
                ('intelligence', models.IntegerField(default=10)),
                ('wisdom', models.IntegerField(default=10)),
                ('charism', models.IntegerField(default=10)),
                ('character_list', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='char_stats', to='character_list.characterlist')),
            ],
            options={
                'verbose_name': 'характеристики_персонажа',
                'verbose_name_plural': 'характеристики_персонажей',
            },
        ),
        migrations.CreateModel(
            name='CharacterAtributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acrobatics', models.IntegerField(blank=True, default=0, null=True)),
                ('athletics', models.IntegerField(blank=True, default=0, null=True)),
                ('training', models.IntegerField(blank=True, default=0, null=True)),
                ('deception', models.IntegerField(blank=True, default=0, null=True)),
                ('history', models.IntegerField(blank=True, default=0, null=True)),
                ('attention', models.IntegerField(blank=True, default=0, null=True)),
                ('intimidation', models.IntegerField(blank=True, default=0, null=True)),
                ('investigation', models.IntegerField(blank=True, default=0, null=True)),
                ('medicine', models.IntegerField(blank=True, default=0, null=True)),
                ('nature', models.IntegerField(blank=True, default=0, null=True)),
                ('insight', models.IntegerField(blank=True, default=0, null=True)),
                ('execution', models.IntegerField(blank=True, default=0, null=True)),
                ('persuasion', models.IntegerField(blank=True, default=0, null=True)),
                ('religion', models.IntegerField(blank=True, default=0, null=True)),
                ('sleight_of_hand', models.IntegerField(blank=True, default=0, null=True)),
                ('stealth', models.IntegerField(blank=True, default=0, null=True)),
                ('survival', models.IntegerField(blank=True, default=0, null=True)),
                ('character_list', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='char_atr', to='character_list.characterlist')),
            ],
            options={
                'verbose_name': 'навыки_персонажа',
                'verbose_name_plural': 'навыки_персонажей',
            },
        ),
    ]
