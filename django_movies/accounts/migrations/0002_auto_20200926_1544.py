# Generated by Django 3.1.1 on 2020-09-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='shoe_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
