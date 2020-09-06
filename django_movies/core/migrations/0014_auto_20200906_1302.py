# Generated by Django 3.1.1 on 2020-09-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200906_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='countries',
            field=models.ManyToManyField(related_name='movies', to='core.Country'),
        ),
    ]