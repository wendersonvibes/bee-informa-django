# Generated by Django 4.2.4 on 2023-10-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0013_alter_cardapios_car_dia_semana'),
    ]

    operations = [
        migrations.AddField(
            model_name='setores',
            name='set_dia_semana',
            field=models.CharField(choices=[('SEG', 'Segunda-feira'), ('TER', 'Terça-feira'), ('QUA', 'Quarta-feira'), ('QUI', 'Quinta-feira'), ('SEX', 'Sexta-feira')], default='SEG', max_length=3, verbose_name='Dia da Semana'),
        ),
    ]
