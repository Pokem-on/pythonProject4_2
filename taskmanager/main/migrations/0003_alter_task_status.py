# Generated by Django 3.2.9 on 2021-12-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.TextField(default=0, verbose_name='Status'),
        ),
    ]
