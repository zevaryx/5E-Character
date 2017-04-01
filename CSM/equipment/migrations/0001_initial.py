# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('material', models.CharField(max_length=128)),
                ('cost_copper', models.SmallIntegerField(blank=True, help_text='Cost in copper pieces.', null=True)),
                ('cost_silver', models.SmallIntegerField(blank=True, help_text='Cost in silver pieces.', null=True)),
                ('cost_gold', models.SmallIntegerField(blank=True, help_text='Cost in gold pieces.', null=True)),
                ('cost_platinum', models.SmallIntegerField(blank=True, help_text='Cost in platinum pieces.', null=True)),
                ('special', models.CharField(blank=True, help_text='General field for additional rules.', max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentBonus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the bonus.', max_length=100, unique=True)),
                ('description', models.CharField(max_length=1024)),
                ('ability_score', models.CharField(blank=True, max_length=16, null=True)),
                ('ability_bonus', models.SmallIntegerField(blank=True, null=True)),
                ('damage_bonus', models.SmallIntegerField(blank=True, null=True)),
                ('damage_dice_number', models.SmallIntegerField(blank=True, null=True)),
                ('damage_dice_size', models.SmallIntegerField(blank=True, null=True)),
                ('advantage', models.BooleanField(default=False)),
                ('disadvantage', models.BooleanField(default=False)),
                ('check', models.CharField(blank=True, max_length=128, null=True)),
                ('skill_bonus', models.SmallIntegerField(blank=True, null=True)),
                ('spell_bonus', models.CharField(blank=True, max_length=128, null=True)),
                ('srd', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
            options={
                'verbose_name': 'Equipment Bonus',
                'verbose_name_plural': 'Equipment Bonuses',
            },
        ),
        migrations.CreateModel(
            name='WeaponProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the weapon property.', max_length=100, unique=True)),
                ('description', models.TextField(help_text='Full description of the weapon property.')),
                ('srd', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
            options={
                'verbose_name': 'Weapon Property',
                'verbose_name_plural': 'Weapon Properties',
            },
        ),
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('equipment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='equipment.Equipment')),
                ('name', models.CharField(help_text='Name of the item.', max_length=100, unique=True)),
                ('armor_type', models.CharField(choices=[('Heavy', 'Heavy Armor'), ('Medium', 'Medium Armor'), ('Light', 'Light Armor'), ('Shield', 'Shield')], max_length=16)),
                ('base_armor_class', models.SmallIntegerField(blank=True, null=True)),
                ('bonus_armor_class', models.SmallIntegerField(blank=True, null=True)),
                ('dexterity_modifier', models.BooleanField(default=True)),
                ('dexterity_modifier_max', models.SmallIntegerField(blank=True, null=True)),
                ('don_time', models.CharField(choices=[('1 action', '1 action'), ('1 minute', '1 minute'), ('5 minutes', '5 minutes'), ('10 minutes', '10 minutes')], max_length=16)),
                ('doff_time', models.CharField(choices=[('1 action', '1 action'), ('1 minute', '1 minute'), ('5 minutes', '5 minutes'), ('10 minutes', '10 minutes')], max_length=16)),
                ('req_str', models.SmallIntegerField(blank=True, null=True)),
                ('stealth_disadvantage', models.BooleanField(default=False)),
                ('srd', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
            options={
                'verbose_name': 'Armor',
                'verbose_name_plural': 'Armor',
            },
            bases=('equipment.equipment',),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('equipment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='equipment.Equipment')),
                ('name', models.CharField(help_text='Name of the item.', max_length=100, unique=True)),
                ('uses', models.SmallIntegerField(blank=True, null=True)),
                ('space', models.CharField(blank=True, max_length=128, null=True)),
                ('srd', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
            bases=('equipment.equipment',),
        ),
        migrations.CreateModel(
            name='MountAndVehicle',
            fields=[
                ('equipment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='equipment.Equipment')),
                ('name', models.CharField(help_text='Name of the item.', max_length=100, unique=True)),
                ('speed', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('carrying_capacity', models.SmallIntegerField(blank=True, null=True)),
                ('vehicle_type', models.CharField(choices=[('Land', 'Land'), ('Water', 'Water'), ('Air', 'Air')], max_length=16)),
                ('srd', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
            options={
                'verbose_name': 'Mount and Vehicle',
                'verbose_name_plural': 'Mounts and Vehicles',
            },
            bases=('equipment.equipment',),
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('equipment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='equipment.Equipment')),
                ('name', models.CharField(help_text='Name of the item.', max_length=100, unique=True)),
                ('requires_proficiency', models.BooleanField(default=False)),
                ('tool_type', models.CharField(max_length=128)),
                ('srd', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
            bases=('equipment.equipment',),
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('equipment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='equipment.Equipment')),
                ('name', models.CharField(help_text='Name of the item.', max_length=100, unique=True)),
                ('weapon_type', models.CharField(choices=[('Simple', 'Simple'), ('Martial', 'Martial')], max_length=16)),
                ('melee_or_ranged', models.CharField(choices=[('Melee', 'Melee'), ('Ranged', 'Ranged')], max_length=16)),
                ('normal_range', models.SmallIntegerField(blank=True, help_text='If a ranged weapon, any attack over normal range is made at disadvantage.', null=True)),
                ('max_range', models.SmallIntegerField(blank=True, help_text='Maximum range a weapon can attack.')),
                ('damage_dice_number', models.SmallIntegerField(help_text='Ex: Xd6 + 1.')),
                ('damage_dice_size', models.SmallIntegerField(help_text='Ex: 1dX + 1.')),
                ('damage_dice_bonus', models.SmallIntegerField(blank=True, help_text='Ex: 1d6 + X.', null=True)),
                ('srd', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
            bases=('equipment.equipment',),
        ),
    ]
