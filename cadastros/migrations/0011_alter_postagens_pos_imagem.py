# Generated by Django 4.2.4 on 2023-10-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0010_alter_postagens_pos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagens',
            name='pos_imagem',
            field=models.ImageField(null=True, upload_to='imagens/', verbose_name='Imagem'),
        ),
    ]
