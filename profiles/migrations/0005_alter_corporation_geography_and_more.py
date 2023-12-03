# Generated by Django 4.2.7 on 2023-12-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0002_bussinessmodel_name_en_bussinessmodel_name_kk_and_more'),
        ('profiles', '0004_startup_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corporation',
            name='geography',
            field=models.ManyToManyField(blank=True, related_name='geography_corporations', to='modules.country', verbose_name='География стартапов'),
        ),
        migrations.AlterField(
            model_name='corporation',
            name='invest_rounds',
            field=models.ManyToManyField(blank=True, related_name='corporations', to='modules.investstage', verbose_name='Раунды инвестиций'),
        ),
        migrations.AlterField(
            model_name='investfund',
            name='geography',
            field=models.ManyToManyField(blank=True, related_name='geography_invest_funds', to='modules.country', verbose_name='География стартапов'),
        ),
        migrations.AlterField(
            model_name='investfund',
            name='invest_rounds',
            field=models.ManyToManyField(blank=True, related_name='invest_funds', to='modules.investstage', verbose_name='Раунды инвестиций'),
        ),
        migrations.AlterField(
            model_name='investor',
            name='geography',
            field=models.ManyToManyField(blank=True, related_name='geography_investors', to='modules.country', verbose_name='География стартапов'),
        ),
        migrations.AlterField(
            model_name='investor',
            name='invest_rounds',
            field=models.ManyToManyField(blank=True, related_name='investors', to='modules.investstage', verbose_name='Раунды инвестиций'),
        ),
    ]
