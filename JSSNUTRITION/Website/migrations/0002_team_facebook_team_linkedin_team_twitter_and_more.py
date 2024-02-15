# Generated by Django 5.0.1 on 2024-01-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='facebook',
            field=models.URLField(blank=True, default='#', null=True, verbose_name='Profil Facebook'),
        ),
        migrations.AddField(
            model_name='team',
            name='linkedin',
            field=models.URLField(blank=True, default='#', null=True, verbose_name='Profil LinkedIn'),
        ),
        migrations.AddField(
            model_name='team',
            name='twitter',
            field=models.URLField(blank=True, default='#', null=True, verbose_name='Profil Twitter'),
        ),
        migrations.AddField(
            model_name='team',
            name='youtube',
            field=models.URLField(blank=True, default='#', null=True, verbose_name='Chaîne YouTube'),
        ),
    ]
