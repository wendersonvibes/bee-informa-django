# Generated by Django 4.2.3 on 2023-10-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setores',
            name='numero_sala',
            field=models.BigIntegerField(),
        ),
    ]
