# Generated by Django 4.2.7 on 2023-11-30 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0002_alter_article_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_en',
            field=models.TextField(null=True, verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='article',
            name='content_kk',
            field=models.TextField(null=True, verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='article',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]
