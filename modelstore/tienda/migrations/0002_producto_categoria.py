# Generated by Django 4.2 on 2023-05-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.CharField(default=None, max_length=20),
        ),
    ]