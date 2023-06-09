# Generated by Django 4.2.2 on 2023-06-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judgeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-score']},
        ),
        migrations.AddField(
            model_name='submission',
            name='language',
            field=models.CharField(choices=[('C++', 'C++'), ('C', 'C'), ('Python3', 'Python3'), ('Python2', 'Python2'), ('Java', 'Java')], default='C++', max_length=10),
        ),
        migrations.AddField(
            model_name='submission',
            name='runtime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='submission',
            name='verdict',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='num_problems_solved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Tough', 'Tough')], max_length=50),
        ),
    ]
