# Generated by Django 4.2.2 on 2023-06-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judgeapp', '0005_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
