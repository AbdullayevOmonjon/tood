# Generated by Django 4.1.6 on 2023-02-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assos_app', '0004_alter_tood_status_delete_talaba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tood',
            name='vaqt',
            field=models.DateTimeField(),
        ),
    ]
