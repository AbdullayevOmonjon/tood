# Generated by Django 4.1.6 on 2023-02-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assos_app', '0003_talaba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tood',
            name='status',
            field=models.BooleanField(blank=True),
        ),
        migrations.DeleteModel(
            name='Talaba',
        ),
    ]
