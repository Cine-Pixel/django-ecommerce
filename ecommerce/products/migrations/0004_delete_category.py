# Generated by Django 4.1.5 on 2023-01-31 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_add_categories'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
