# Generated by Django 5.2 on 2025-04-09 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('spellLevelType', models.CharField(blank=True, max_length=255, null=True)),
                ('castingTime', models.CharField(blank=True, max_length=50, null=True)),
                ('spellRange', models.CharField(blank=True, max_length=50, null=True)),
                ('components', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('spellList', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
