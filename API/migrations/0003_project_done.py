# Generated by Django 4.1.1 on 2022-10-29 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
