# Generated by Django 4.0.2 on 2022-02-15 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_categories_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categories',
        ),
    ]