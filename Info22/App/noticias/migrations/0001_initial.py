# Generated by Django 4.1.3 on 2022-12-22 04:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=80)),
                ('tipo_de_consulta', models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'sugerencia'], [3, 'felicitaciones']], default='0')),
                ('mensaje', models.TextField()),
                ('desea_recibir_avisos', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('Email', models.EmailField(default=' ', max_length=254)),
                ('imagen', models.ImageField(blank=True, default='noticia/default.png', null=True, upload_to='noticia')),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('comentario', models.TextField(default='', max_length=200)),
                ('segundo_comentario', models.CharField(default=' ', max_length=100)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticias.categoria')),
            ],
            options={
                'ordering': ('publicado',),
            },
        ),
    ]
