# Generated by Django 4.0.2 on 2022-03-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='STATUS_DISPLAY',
            field=models.BooleanField(default=True, verbose_name='Вывод пользователя в статистике подразделения'),
        ),
    ]
