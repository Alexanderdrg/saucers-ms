# Generated by Django 5.0.2 on 2024-02-15 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saucers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saucer',
            name='additional',
            field=models.ManyToManyField(to='saucers.additional'),
        ),
        migrations.AddField(
            model_name='saucer',
            name='ingredients',
            field=models.ManyToManyField(to='saucers.ingredient'),
        ),
    ]
