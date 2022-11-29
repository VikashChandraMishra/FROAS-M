# Generated by Django 4.1.1 on 2022-11-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tau', '0010_delete_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher', models.IntegerField()),
                ('course', models.CharField(max_length=30)),
                ('semester', models.IntegerField()),
                ('subject', models.CharField(max_length=30)),
                ('attendance', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('students', models.ManyToManyField(to='tau.student')),
            ],
        ),
    ]