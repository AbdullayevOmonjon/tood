# Generated by Django 4.1.7 on 2023-02-16 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tood',
            name='nom',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='tood',
            name='vaqt',
            field=models.DateField(),
        ),
    ]
