# Generated by Django 3.2.7 on 2022-05-05 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_alter_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='branch',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='enrollment',
            field=models.CharField(max_length=30),
        ),
    ]
