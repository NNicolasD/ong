# Generated by Django 4.1.3 on 2022-12-03 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_alter_noticia_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='segundo_comentario',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
