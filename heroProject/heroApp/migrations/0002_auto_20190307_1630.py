# Generated by Django 2.2 on 2019-03-07 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heroappmodel',
            old_name='name',
            new_name='Name',
        ),
        migrations.AddField(
            model_name='heroappmodel',
            name='question1',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='heroappmodel',
            name='question2',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='heroappmodel',
            name='question3',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='heroappmodel',
            name='question4',
            field=models.TextField(default=0, max_length=1000),
        ),
    ]