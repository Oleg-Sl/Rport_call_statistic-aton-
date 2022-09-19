# Generated by Django 4.0.2 on 2022-04-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityapp', '0012_callsplan_plan_completed_comment_date_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='CREATED',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Дата создания дела'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='DIRECTION',
            field=models.CharField(choices=[('0', '-'), ('1', 'Входящее'), ('2', 'Исходящее')], db_index=True, max_length=1, verbose_name='Направление дела (входящее/исходящее)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='TYPE_ID',
            field=models.CharField(choices=[('1', 'Встреча'), ('2', 'Звонок'), ('3', 'Задача'), ('4', 'Письмо')], db_index=True, max_length=1, verbose_name='Тип дела (входящее/исходящее)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Дело не удалено из Битрикс24'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='CALL_DURATION',
            field=models.PositiveIntegerField(db_index=True, verbose_name='Длительность звонка'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ACTIVE',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Пользователь активен (не уволен)'),
        ),
        migrations.AlterField(
            model_name='user',
            name='STATUS_DISPLAY',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Вывод пользователя в статистике подразделения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='UF_DEPARTMENT',
            field=models.PositiveIntegerField(db_index=True, verbose_name='ID департамета'),
        ),
    ]
