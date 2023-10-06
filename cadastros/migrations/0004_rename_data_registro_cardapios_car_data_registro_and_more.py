# Generated by Django 4.2.4 on 2023-10-06 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_alter_setores_numero_sala'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardapios',
            old_name='data_registro',
            new_name='car_data_registro',
        ),
        migrations.RenameField(
            model_name='cardapios',
            old_name='descricao',
            new_name='car_descricao',
        ),
        migrations.RenameField(
            model_name='cardapios',
            old_name='dia_semana',
            new_name='car_dia_semana',
        ),
        migrations.RenameField(
            model_name='categorias',
            old_name='categoria',
            new_name='cat_categoria',
        ),
        migrations.RenameField(
            model_name='postagens',
            old_name='categoria',
            new_name='pos_cat_codigo',
        ),
        migrations.RenameField(
            model_name='postagens',
            old_name='conteudo',
            new_name='pos_conteudo',
        ),
        migrations.RenameField(
            model_name='postagens',
            old_name='data_registro',
            new_name='pos_data_registro',
        ),
        migrations.RenameField(
            model_name='postagens',
            old_name='titulo',
            new_name='pos_titulo',
        ),
        migrations.RenameField(
            model_name='setores',
            old_name='nome',
            new_name='set_nome',
        ),
        migrations.RenameField(
            model_name='setores',
            old_name='numero_sala',
            new_name='set_numero_sala',
        ),
        migrations.RenameField(
            model_name='setores',
            old_name='representante',
            new_name='set_representante',
        ),
    ]
