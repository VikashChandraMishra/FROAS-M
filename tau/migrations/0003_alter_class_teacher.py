# Generated by Django 4.1.1 on 2022-11-06 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tau', '0002_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='teacher',
            field=models.IntegerField(),
        ),
    ]