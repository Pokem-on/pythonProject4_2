# Generated by Django 3.2.9 on 2021-12-03 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211203_1908'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Taska',
            new_name='Task',
        ),
    ]