# Generated by Django 4.2 on 2023-05-08 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicio',
            options={'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
        migrations.AlterField(
            model_name='servicio',
            name='contenido',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='Servicios'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
