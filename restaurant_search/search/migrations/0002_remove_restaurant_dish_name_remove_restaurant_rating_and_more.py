# Generated by Django 5.0.7 on 2024-07-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='dish_name',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='rating',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='dish',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]